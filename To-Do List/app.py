import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")

def update_task():
    try:
        index = listbox.curselection()
        selected_task = listbox.get(index)
        updated_task = entry.get()
        if updated_task:
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter an updated task.")
    except:
        messagebox.showwarning("No Task Selected", "Please select a task to update.")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

# Create listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Create entry box
entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=5)

# Create buttons with color
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="skyblue", fg="white")
add_button.grid(row=0, column=0)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="red", fg="white")
delete_button.grid(row=0, column=1)

update_button = tk.Button(button_frame, text="Update Task", command=update_task, bg="green", fg="white")
update_button.grid(row=0, column=2)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks, bg="black", fg="white")
clear_button.grid(row=0, column=3)

root.mainloop()
