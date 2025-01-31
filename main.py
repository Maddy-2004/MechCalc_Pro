import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("MechCalcPro", "Welcome to MechCalcPro!")

# Create GUI window
root = tk.Tk()
root.title("MechCalcPro")
root.geometry("300x200")

# Add button
btn = tk.Button(root, text="Click Me", command=show_message)
btn.pack(pady=50)

# Run application
root.mainloop()
