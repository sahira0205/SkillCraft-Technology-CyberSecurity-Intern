# Caesar Cipher Program

This repository contains a Python script that implements the Caesar Cipher, an early and simple method of encryption. The program can encrypt a plaintext message or decrypt a ciphertext message given a specific shift key.

This project was created to fulfill "Task 01" from a cybersecurity learning module.

## 🚀 Features

* **Encryption:** Converts a plain message into a secret ciphertext.
* **Decryption:** Converts ciphertext back into the original message.
* **Custom Shift Key:** The user can provide any numerical shift value.
* **Case Preservation:** Correctly handles both uppercase and lowercase letters (e.g., 'A' shifts to 'D' and 'a' shifts to 'd').
* **Character Handling:** Ignores and preserves all non-alphabetic characters (spaces, punctuation, numbers, etc.).

## ⚙️ How to Use

You can run this script from any terminal that has Python 3 installed.

1.  **Clone or Download**
    * Clone the repository:
        ```bash
        git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
        ```
    * Or, simply download the `caesar_cipher.py` file.

2.  **Navigate to the Directory**
    ```bash
    cd YOUR_REPOSITORY_NAME
    ```

3.  **Run the Script**
    ```bash
    python caesar_cipher.py
    ```
    *(Note: You may need to use `python3` instead of `python` on some systems).*

4.  **Follow the Prompts**
    The program will ask you to:
    * Enter your message.
    * Enter the shift value.
    * Choose to (e)ncrypt or (d)ecrypt.

### Example

**Encryption:**
Enter your message: Hello, World! Enter the shift value (a number): 3 Do you want to (e)ncrypt or (d)ecrypt? e

--- Result --- Result: Khoor, Zruog!


**Decryption:**
Enter your message: Khoor, Zruog! Enter the shift value (a number): 3 Do you want to (e)ncrypt or (d)ecrypt? d

--- Result --- Result: Hello, World!