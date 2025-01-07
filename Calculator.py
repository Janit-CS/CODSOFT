import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

app = tk.Tk()
app.title("Styled Calculator")
app.geometry("350x350")
app.config(bg="#f0f0f0")

label_num1 = tk.Label(app, text="Enter first number:", font=("Arial", 12), bg="#f0f0f0")
label_num1.pack(pady=10)
entry_num1 = tk.Entry(app, font=("Arial", 12), width=20)
entry_num1.pack(pady=5)

label_num2 = tk.Label(app, text="Enter second number:", font=("Arial", 12), bg="#f0f0f0")
label_num2.pack(pady=10)
entry_num2 = tk.Entry(app, font=("Arial", 12), width=20)
entry_num2.pack(pady=5)

operation_var = tk.StringVar(app)
operation_var.set("Add")
operations_menu = tk.OptionMenu(app, operation_var, "Add", "Subtract", "Multiply", "Divide")
operations_menu.config(font=("Arial", 12), width=18)
operations_menu.pack(pady=10)

button_calculate = tk.Button(app, text="Calculate", font=("Arial", 12), bg="#4CAF50", fg="white", command=perform_calculation)
button_calculate.pack(pady=20)

label_result = tk.Label(app, text="Result: ", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_result.pack(pady=10)

app.mainloop()