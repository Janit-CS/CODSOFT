import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 8:
            label_result.config(text="Password length should be at least 8 characters.", fg="red")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        label_result.config(text=f"Generated Password: {password}", fg="green")
    except ValueError:
        label_result.config(text="Please enter a valid number for the password length.", fg="red")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

label_prompt = tk.Label(root, text="Enter the desired password length:", font=("Arial", 12), bg="#f0f0f0")
label_prompt.pack(pady=10)

entry_length = ttk.Entry(root, font=("Arial", 12), width=20)
entry_length.pack(pady=5)

button_generate = ttk.Button(root, text="Generate Password", command=generate_password, style="TButton")
button_generate.pack(pady=10)

label_result = tk.Label(root, text="Generated Password will appear here", font=("Arial", 12), bg="#f0f0f0", wraplength=300)
label_result.pack(pady=10)

style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12),
                background="#4CAF50",
                foreground="black",
                padding=10)

root.mainloop()