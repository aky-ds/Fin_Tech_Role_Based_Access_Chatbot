import os
from dotenv import load_dotenv
load_dotenv()

# Getting the admin credentials from environment variables
# or using default values if not set
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

def is_admin(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD
