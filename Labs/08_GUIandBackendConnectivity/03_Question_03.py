# Design a GUI for student registration for a course and store these details in a database. 
# Use Tkinter for UI, SQLite/MySQL for database storage.

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def register():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    course = course_entry.get()

    if name == "" or age == "" or gender == "" or email == "" or course == "":
        messagebox.showerror("Error", "All fields are required")
        return

    cursor.execute(
        "INSERT INTO students(name, age, gender, email, course) VALUES (?, ?, ?, ?, ?)",
        (name, age, gender, email, course)
    )
    conn.commit()

    messagebox.showinfo("Success", "Student Registered Successfully")

    # Clear fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    gender_var.set("")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student Course Registration")
root.geometry("400x400")

tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold")).pack(pady=10)

# Name
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Age
tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack()

# Gender
tk.Label(root, text="Gender").pack()
gender_var = tk.StringVar()

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Email
tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack()

# Course
tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root, width=30)
course_entry.pack()

# Register Button
tk.Button(root, text="Register", width=20, bg="green", fg="white",
          command=register).pack(pady=20)

root.mainloop()

# Close DB after window closes
conn.close()