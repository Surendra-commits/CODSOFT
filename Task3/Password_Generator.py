import random
import string
import tkinter as tk
from tkinter import messagebox, filedialog
import pyperclip


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("450x550")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Password Generator", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.length_label = tk.Label(root, text="Enter password length:", font=("Helvetica", 12), bg="#f0f0f0")
        self.length_label.pack()

        self.length_entry = tk.Entry(root, font=("Helvetica", 12))
        self.length_entry.pack(pady=5)

        self.uppercase_var = tk.IntVar()
        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.uppercase_var,
                                              font=("Helvetica", 12), bg="#f0f0f0")
        self.uppercase_check.pack()

        self.digits_var = tk.IntVar()
        self.digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.digits_var,
                                           font=("Helvetica", 12), bg="#f0f0f0")
        self.digits_check.pack()

        self.special_var = tk.IntVar()
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_var,
                                            font=("Helvetica", 12), bg="#f0f0f0")
        self.special_check.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password,
                                         font=("Helvetica", 14, "bold"), bg="#0074D9", fg="white")
        self.generate_button.pack(pady=20)

        self.strength_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        self.strength_label.pack()

        self.result_frame = tk.Frame(root, bg="#f0f0f0")
        self.result_label = tk.Label(self.result_frame, text="", font=("Helvetica", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard,
                                     font=("Helvetica", 12), bg="#2ECC40", fg="white")
        self.copy_button.pack()

        self.save_button = tk.Button(root, text="Save to File", command=self.save_to_file, font=("Helvetica", 12),
                                     bg="#FF4136", fg="white")
        self.save_button.pack()

        self.result_frame.pack()

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                messagebox.showerror("Error", "Password length must be greater than zero.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
            return

        characters = string.ascii_lowercase  # Always include lowercase letters

        if self.uppercase_var.get():
            characters += string.ascii_uppercase

        if self.digits_var.get():
            characters += string.digits

        if self.special_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one option.")
            return

        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.result_label.config(text="Generated Password: " + generated_password)
        self.generated_password = generated_password  # Store the generated password

        # Evaluate password strength and provide feedback
        strength = self.evaluate_password_strength(generated_password)
        self.strength_label.config(text="Password Strength: " + strength)

    def evaluate_password_strength(self, password):
        length = len(password)
        if length < 8:
            return "Weak"
        elif length < 12:
            return "Moderate"
        elif length < 16:
            return "Strong"
        else:
            return "Very Strong"

    def copy_to_clipboard(self):
        try:
            pyperclip.copy(self.generated_password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        except AttributeError:
            messagebox.showerror("Error", "No password generated yet.")

    def save_to_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write("Generated Password: " + self.generated_password)
                messagebox.showinfo("Success", "Password saved to file!")
        except AttributeError:
            messagebox.showerror("Error", "No password generated yet.")


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
