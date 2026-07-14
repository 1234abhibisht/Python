# Design a login and signup authentication system.

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def signup():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        messagebox.showinfo("Success", "Signup Successful")
        clear_fields()
    except:
        messagebox.showerror("Error", "Username already exists")


def login():
    username = user_entry.get()
    password = pass_entry.get()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Login Successful")
        clear_fields()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def clear_fields():
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Login & Signup System")
root.geometry("350x250")

tk.Label(root, text="Authentication System",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
user_entry = tk.Entry(root, width=30)
user_entry.pack()

tk.Label(root, text="Password").pack()
pass_entry = tk.Entry(root, width=30, show="*")
pass_entry.pack(pady=5)

tk.Button(root, text="Login", width=15, bg="blue", fg="white",
          command=login).pack(pady=5)

tk.Button(root, text="Signup", width=15, bg="green", fg="white",
          command=signup).pack(pady=5)

root.mainloop()

conn.close()