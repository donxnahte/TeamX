#Mwangi Erick
#25.02.2026

# MWANGI ERICK
# School Management System with Tkinter
# 25.02.2026

import tkinter as tk
from tkinter import messagebox, filedialog

students = []

# Function to add student
def add_student():
    student_id = entry_id.get()
    first_name = entry_fname.get()
    last_name = entry_lname.get()
    courses = entry_courses.get()
    phone = entry_phone.get()

    if student_id == "" or first_name == "" or last_name == "" or courses == "" or phone == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    student = {
        "ID": student_id,
        "First Name": first_name,
        "Last Name": last_name,
        "Courses": courses,
        "Phone": phone
    }

    students.append(student)
    listbox.insert(tk.END, f"{student_id} - {first_name} {last_name}")

    clear_fields()
    messagebox.showinfo("Success", "Student added successfully!")

# Function to clear fields
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_fname.delete(0, tk.END)
    entry_lname.delete(0, tk.END)
    entry_courses.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# Function to export students to text file
def export_students():
    if not students:
        messagebox.showwarning("No Data", "No students to export!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])

    if file_path:
        with open(file_path, "w") as file:
            for student in students:
                file.write(f"Student ID: {student['ID']}\n")
                file.write(f"First Name: {student['First Name']}\n")
                file.write(f"Last Name: {student['Last Name']}\n")
                file.write(f"Courses: {student['Courses']}\n")
                file.write(f"Phone: {student['Phone']}\n")
                file.write("-" * 40 + "\n")

        messagebox.showinfo("Exported", "Students exported successfully!")

# GUI Window
root = tk.Tk()
root.title("School Management System")
root.geometry("500x500")

# Labels and Entry Fields
tk.Label(root, text="Student ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="First Name").pack()
entry_fname = tk.Entry(root)
entry_fname.pack()

tk.Label(root, text="Last Name").pack()
entry_lname = tk.Entry(root)
entry_lname.pack()

tk.Label(root, text="Courses (comma separated)").pack()
entry_courses = tk.Entry(root)
entry_courses.pack()

tk.Label(root, text="Phone Number").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Export to Text File", command=export_students).pack(pady=5)

# Listbox to display students
tk.Label(root, text="Students Added").pack()
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()