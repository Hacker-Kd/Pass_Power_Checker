import re
import hashlib
import random
import string
import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    # Minimum length requirement
    min_length = 8

    # Regular expressions for checking complexity
    has_lowercase = re.search(r'[a-z]', password)
    has_uppercase = re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[^a-zA-Z0-9]', password)

    # Check password length
    if len(password) < min_length:
        return "Weak - Password length should be at least {} characters.".format(min_length)

    # Check complexity
    complexity = 0
    if has_lowercase:
        complexity += 1
    if has_uppercase:
        complexity += 1
    if has_digit:
        complexity += 1
    if has_special:
        complexity += 1

    # Evaluate password strength
    if complexity == 1:
        return "Weak - Password should include a mix of uppercase, lowercase, digits, and special characters."
    elif complexity == 2:
        return "Moderate - Password is okay, but could be stronger with a mix of uppercase, lowercase, digits, and special characters."
    elif complexity >= 3:
        return "Strong - Good job! Your password is strong and secure."
    else:
        return "Weak - Password should include a mix of uppercase, lowercase, digits, and special characters."

def store_password(password):
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # In a real-world scenario, you would store the hashed password securely in a database

def generate_password():
    # Generate a secure random password with a mix of uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    return password

def check_password():
    password = password_entry.get()
    strength_feedback = assess_password_strength(password)
    store_password(password)
    messagebox.showinfo("Password Strength", strength_feedback)

def generate_and_show_password():
    password = generate_password()
    messagebox.showinfo("Generated Password", "Your secure password is:\n{}".format(password))

# Create a simple GUI using Tkinter
root = tk.Tk()
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter your password:")
label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack()

generate_button = tk.Button(root, text="Generate Secure Password", command=generate_and_show_password)
generate_button.pack()

root.mainloop()
