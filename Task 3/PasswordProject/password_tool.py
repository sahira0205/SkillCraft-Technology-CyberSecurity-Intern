import tkinter as tk
from tkinter import messagebox
import re

def check_password_logic():
    password = password_entry.get()
    
    strength_score = 0
    feedback = []
    
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("• Too short (needs 8+ chars)")

    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("• Missing uppercase (A-Z)")

    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("• Missing lowercase (a-z)")

    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("• Missing numbers (0-9)")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("• Missing special chars (!@#$)")

    if strength_score == 5:
        result_label.config(text="STRENGTH: VERY STRONG", fg="#2ecc71")
        feedback_label.config(text="Excellent! This is a secure password.")
    elif strength_score >= 3:
        result_label.config(text="STRENGTH: MODERATE", fg="#f1c40f")
        feedback_label.config(text="Suggestions:\n" + "\n".join(feedback))
    else:
        result_label.config(text="STRENGTH: WEAK", fg="#e74c3c")
        feedback_label.config(text="Suggestions:\n" + "\n".join(feedback))

def toggle_password():
    if show_pass_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

root = tk.Tk()
root.title("CyberSec Password Analyzer")
root.geometry("500x450")
root.configure(bg="#2c3e50")

title_label = tk.Label(root, text="PASSWORD STRENGTH TEST", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=30)

input_frame = tk.Frame(root, bg="#2c3e50")
input_frame.pack(pady=10)

password_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=25, bd=0, highlightthickness=1)
password_entry.pack(pady=5, ipady=5)

show_pass_var = tk.BooleanVar(value=True)
show_pass_check = tk.Checkbutton(root, text="Show Password", variable=show_pass_var, 
                                 command=toggle_password, bg="#2c3e50", fg="white", 
                                 selectcolor="#2c3e50", activebackground="#2c3e50", activeforeground="white")
show_pass_check.pack(pady=5)

check_button = tk.Button(root, text="CHECK STRENGTH", font=("Helvetica", 12, "bold"), 
                         bg="#3498db", fg="white", activebackground="#2980b9", 
                         activeforeground="white", width=20, bd=0, command=check_password_logic)
check_button.pack(pady=20)

result_frame = tk.Frame(root, bg="#34495e", padx=20, pady=20)
result_frame.pack(fill="x", padx=30)

result_label = tk.Label(result_frame, text="ENTER A PASSWORD", font=("Helvetica", 14, "bold"), bg="#34495e", fg="#ecf0f1")
result_label.pack()

feedback_label = tk.Label(result_frame, text="", font=("Helvetica", 10), bg="#34495e", fg="#bdc3c7", justify="left")
feedback_label.pack(pady=10)

root.mainloop()