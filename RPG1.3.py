import tkinter as tk
from tkinter import messagebox
import random
import string
import os
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator - RPG 1.3")
        self.root.geometry("600x400")
        self.root.configure(bg="#3A3B3C")

        self.generate_button = tk.Button(root, text="Generate a random password", command=self.generate_password, font=('Helvetica', 14), bg="#6D7B8D", fg="#690d3b")
        self.generate_button.pack(pady=15)

        self.password_label = tk.Label(root, text="Your password is:", font=("Helvetica", 14), fg="#C9C0BB", bg="#690d3b")
        self.password_label.pack(pady=10)

        self.password_display = tk.Entry(root, width=20, show="*", font=("Helvetica", 18))
        self.password_display.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy to clipboard", command=self.copy_to_clipboard, font=("Helvetica", 14), bg="#6D7B8D", fg="#690d3b")
        self.copy_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save password", command=self.save_password, font=("Helvetica", 16), bg="#6D7B8D", fg="#690d3b")
        self.save_button.pack(pady=20)

        self.license_label = tk.Label(root, text="License: GPL3", font=("Helvetica", 8), fg="white", bg="#3A3B3C")
        self.license_label.pack(side=tk.RIGHT, padx=10, pady=5)

    def generate_password(self):
        password_length = random.randint(8, 14)
        characters = string.ascii_letters + string.digits
        generated_password = ''.join(random.choice(characters) for i in range(password_length))

        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, generated_password)

    def copy_to_clipboard(self):
        password = self.password_display.get()
        pyperclip.copy(password)  
        messagebox.showinfo("Copying to clipboard", 'Your password has been copied \nto clipboard!')

    def save_password(self):
        password = self.password_display.get()
        desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
        filename = os.path.join(desktop_path, "generated_password.txt")

        with open(filename, "a") as file:
            file.write(password + "\n")
        messagebox.showinfo('Password storage', 'Your password is \nsaved in a file named "generated_password.txt" \non Desktop')

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
