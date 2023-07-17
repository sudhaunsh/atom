import sqlite3

def login(usr, pwd):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    #create a table called users with columns username and password
    # c.execute("CREATE TABLE users (username TEXT, password TEXT)")
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (usr, pwd))
    if c.fetchone() is not None:
        return True
    else:
        return False

def create_account(usr, pwd):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (usr, pwd))
    conn.commit()
    conn.close()

# create_account("Sudhulyf", "1234")
