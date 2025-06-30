import os
import glob
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# -------------------------------------------------------------------
# 1️⃣ Load Env Variables
# -------------------------------------------------------------------
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# -------------------------------------------------------------------
# 2️⃣ Init Embeddings and Chroma Client
# -------------------------------------------------------------------
embedding_fn = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
client = chromadb.PersistentClient(path="./chroma_db")  # ✅ Persistent storage
vectorstore = Chroma(client=client, collection_name="fin_hr", embedding_function=embedding_fn)

# -------------------------------------------------------------------
# 3️⃣ Load Markdown files and Add if empty
# -------------------------------------------------------------------
files = glob.glob("data/*/*.md")  # Adjust path accordingly
texts, ids = [], []
for i, filepath in enumerate(files):
    role_name = os.path.basename(os.path.dirname(filepath)).lower()
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        texts.append(f"ROLE:{role_name}\n{content}")
        ids.append(str(i))

# Add texts only if the database is empty
if vectorstore._collection.count() == 0:
    print(f"Adding {len(texts)} documents to the database...")
    vectorstore.add_texts(texts, ids=ids)

# -------------------------------------------------------------------
# 4️⃣ Chat Model & RetrievalQA
# -------------------------------------------------------------------
llm = ChatGroq(model="llama3-70b-8192")  # Chat model
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# -------------------------------------------------------------------
# 5️⃣ Final Role-Based Answer Function
# -------------------------------------------------------------------
def get_answer_for_role(user_role: str, query: str) -> str:
    """Retrieve an answer for the specific role."""
    results = qa.retriever.get_relevant_documents(query)

    # ✅ Filter documents for the role
    role_docs = [doc for doc in results if f"ROLE:{user_role}" in doc.page_content]
    if not role_docs:
        return "You don't have access to this data."

    # ✅ Combine role_docs and send to the LLM
    combined_docs = '\n'.join(doc.page_content for doc in role_docs)
    answer = llm.invoke(f"Context:\n{combined_docs}\n\nQuestion: {query}")

    return answer.content
