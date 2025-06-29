import sqlite3

# initialize the database and create the users table if it doesn't exist
def init_db():
    conn = sqlite3.connect("database/app_data.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Function to add or update a user in the database
# If the user already exists, it will update the password and role
def add_user(username, password, role):
    conn = sqlite3.connect("database/app_data.db")
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO users (username, password, role) VALUES (?, ?, ?)",
              (username, password, role))
    conn.commit()
    conn.close()

# Function to delete a user from the database
# It will remove the user with the specified username
def delete_user(username):
    conn = sqlite3.connect("database/app_data.db")
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()
    conn.close()

# Function to retrieve a user's role based on username and password
# It will return the role of the user if found, otherwise None
def get_user(username, password):
    conn = sqlite3.connect("database/app_data.db")
    c = conn.cursor()
    c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
