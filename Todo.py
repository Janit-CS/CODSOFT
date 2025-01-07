import tkinter as tk
from tkinter import ttk, messagebox
import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['name']} (Due: {task['due_date']}, Priority: {task['priority']})")

def add_task():
    name = task_name_entry.get().strip()
    due_date = task_due_date_entry.get().strip()
    priority = task_priority_combobox.get().strip().capitalize()
    if not name or not due_date or not priority:
        messagebox.showwarning("Input Error", "All fields must be filled out!")
        return
    tasks.append({"name": name, "due_date": due_date, "priority": priority, "completed": False})
    save_tasks(tasks)
    refresh_task_list()
    task_name_entry.delete(0, tk.END)
    task_due_date_entry.delete(0, tk.END)
    task_priority_combobox.set("")
    messagebox.showinfo("Task Added", f"Task '{name}' added successfully!")

def mark_task_completed():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")
        return
    tasks[selected_index[0]]["completed"] = True
    save_tasks(tasks)
    refresh_task_list()
    messagebox.showinfo("Task Updated", "Task marked as completed!")

def delete_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        return
    deleted_task = tasks.pop(selected_index[0])
    save_tasks(tasks)
    refresh_task_list()
    messagebox.showinfo("Task Deleted", f"Task '{deleted_task['name']}' deleted successfully!")

tasks = load_tasks()

app = tk.Tk()
app.title("To-Do List Application")
app.geometry("500x450")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TEntry", font=("Arial", 10))
style.configure("TCombobox", font=("Arial", 10))

frame = ttk.Frame(app, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

task_listbox = tk.Listbox(frame, height=15, width=60, selectmode=tk.SINGLE, font=("Arial", 10))
task_listbox.pack(pady=10, anchor="center")
refresh_task_list()

input_frame = ttk.Frame(frame)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Task Name:").grid(row=0, column=0, padx=5, pady=5)
task_name_entry = ttk.Entry(input_frame, width=25)
task_name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
task_due_date_entry = ttk.Entry(input_frame, width=25)
task_due_date_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Priority:").grid(row=2, column=0, padx=5, pady=5)
task_priority_combobox = ttk.Combobox(input_frame, values=["Low", "Medium", "High"], state="readonly", width=23)
task_priority_combobox.grid(row=2, column=1, padx=5, pady=5)

button_frame = ttk.Frame(frame)
button_frame.pack(pady=10)

add_task_button = ttk.Button(button_frame, text="Add Task", command=add_task, width=15)
add_task_button.grid(row=0, column=0, padx=5, pady=5)

mark_completed_button = ttk.Button(button_frame, text="Mark Completed", command=mark_task_completed, width=15)
mark_completed_button.grid(row=0, column=1, padx=5, pady=5)

delete_task_button = ttk.Button(button_frame, text="Delete Task", command=delete_task, width=15)
delete_task_button.grid(row=0, column=2, padx=5, pady=5)

app.mainloop()