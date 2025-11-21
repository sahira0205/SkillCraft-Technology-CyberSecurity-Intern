# Password Strength Assessment Tool 🔐

A GUI-based application built with Python that analyzes the complexity of passwords and provides real-time feedback on their strength.

## 📋 Project Overview
This tool was developed as part of my Cybersecurity Internship (**Task 03**). It serves as a practical implementation of input validation and password policy enforcement.

The application checks the user's input against standard security criteria (length, variety of characters) and assigns a strength rating: **Weak**, **Moderate**, or **Very Strong**.

## ✨ Key Features
* **Graphical User Interface (GUI):** Built with `Tkinter` for a user-friendly experience.
* **Dark Mode Design:** A modern, professional interface using a slate-blue color palette.
* **Real-Time Feedback:** Provides specific suggestions on how to improve the password (e.g., "Missing special characters").
* **Privacy Control:** Includes a "Show/Hide Password" toggle button.
* **Scoring Algorithm:** Uses Regular Expressions (`re`) to detect:
    * Length (8+ characters)
    * Uppercase Letters (A-Z)
    * Lowercase Letters (a-z)
    * Numbers (0-9)
    * Special Characters (!@#$...)

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Libraries:**
    * `tkinter` (Standard GUI library)
    * `re` (Regular Expressions for pattern matching)

## 🚀 How to Run
No external installation (`pip install`) is required as this uses Python's standard libraries.

1.  **Clone or Download** this repository.
2.  Open your terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the script:
    ```bash
    python password_tool.py
    ```

## 🧠 How the Logic Works
The password starts with a score of 0. The algorithm checks five conditions:
1.  **Length Check:** Is the password ≥ 8 characters? (+1 Point)
2.  **Upper Case Check:** Does it contain 'A-Z'? (+1 Point)
3.  **Lower Case Check:** Does it contain 'a-z'? (+1 Point)
4.  **Numeric Check:** Does it contain '0-9'? (+1 Point)
5.  **Symbol Check:** Does it contain special characters? (+1 Point)

**Grading Scale:**
* **5 Points:** Very Strong (Green)
* **3-4 Points:** Moderate (Yellow)
* **0-2 Points:** Weak (Red)

*Disclaimer: This tool is for educational purposes to demonstrate password complexity logic.*