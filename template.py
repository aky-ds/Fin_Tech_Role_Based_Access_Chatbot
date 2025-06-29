import os 
from pathlib import Path

list_of_files = [
    'setup.py',
    'README.md',
    'requirements.txt',
    'streamlit_app.py',
    'database/__init__.py',
    'database/db.py',
    'chat/__init__.py',
    'chat/chat.py',
    'embeddings/__init__.py',
    'embeddings/embeddings.py'
    'auth.py',
    
]
for file in list_of_files:
    file_path=Path(file)
    file_dir,file_name=os.path.split(file_path)
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
    
    if not os.path.exists(file_path):
        with open(file_path,'w') as f:
            pass