import streamlit as st
import base64
from database.db import init_db, add_user, delete_user, get_user
from auth_admin import is_admin
from embeddings.embeddings import get_answer_for_role

# Initialize DB
init_db()

def set_background(image_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
        }}
        .title-text {{
            font-size: 36px;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-top: 30px;
            margin-bottom: 0;
            text-shadow: 2px 2px 4px #000;
        }}
        
        .login-box h2, .section h2, .section h3 {{
            color: white;
            background-color: transparent;
            text-shadow: 1px 1px 3px #000;
        }}
        label {{
            color: black !important;
            font-weight: 500;
        }}
        </style>
    """, unsafe_allow_html=True)

# Set background
set_background("data/bg.png")

# Title
st.markdown("<div class='title-text'>🗄️ FinSolve Role-Based Chatbot</div>", unsafe_allow_html=True)

# Session State Init
if "user" not in st.session_state:
    st.session_state["user"] = None
    st.session_state["role"] = None

# Login Page
if not st.session_state["user"]:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.markdown('<h2 style="color: Black;">👤 Login</h2>', unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        role = get_user(username, password)
        if role:
            st.session_state["user"] = username
            st.session_state["role"] = role
            st.success(f"✅ Logged in as {username} ({role})")
        elif is_admin(username, password):
            st.session_state["user"] = username
            st.session_state["role"] = "admin"
            st.success("✅ Logged in as Admin")
        else:
            st.error("❌ Invalid credentials.")
    st.markdown("</div>", unsafe_allow_html=True)

# Admin View
elif st.session_state["role"] == "admin":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown('<h3 style="color: Black;">👥 User Management</h3>', unsafe_allow_html=True)
    action = st.selectbox("Action:", ["Add User", "Delete User"])
    if action == "Add User":
        new_user = st.text_input("New Username")
        new_pwd = st.text_input("New User Password", type="password")
        new_role = st.selectbox("Assign Role", ["finance", "marketing", "hr", "engineering", "general", "c-level"])
        if st.button("Add User"):
            add_user(new_user, new_pwd, new_role)
            st.success(f"✅ User `{new_user}` added successfully.")
    elif action == "Delete User":
        del_user = st.text_input("Username to Delete")
        if st.button("Delete User"):
            delete_user(del_user)
            st.success(f"🗑️ User `{del_user}` deleted.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown('<h3 style="color: Black;">💬 Admin Chat (C-Level Access)</h3>', unsafe_allow_html=True)
    query = st.text_area("Enter your query:", key="admin_query")
    if st.button("Send as Admin"):
        if query:
            answer = get_answer_for_role("c-level", query)
            st.success("💡 Response:")
            st.write(answer)
    st.markdown("</div>", unsafe_allow_html=True)

# User View
else:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader(f"💬 Chat as [{st.session_state['role']}]")
    query = st.text_area("Enter your query:", key="user_query")
    if st.button("Send"):
        if query:
            answer = get_answer_for_role(st.session_state["role"], query)
            st.success("💡 Response:")
            st.markdown(f'<p style="color: black;">{answer}</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Logout
st.markdown("<div class='section'>", unsafe_allow_html=True)
if st.button("🚪 Logout"):
    st.session_state["user"] = None
    st.session_state["role"] = None
    st.experimental_rerun()
st.markdown("</div>", unsafe_allow_html=True)
