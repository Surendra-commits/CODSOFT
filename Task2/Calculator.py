import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(root, font=("Helvetica", 18), justify="right", textvariable=self.result_var)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 1, 4), ("√", 2, 4), ("^", 3, 4), ("π", 4, 4)
        ]

        for button_text, row, column in self.buttons:
            button = tk.Button(root, text=button_text, font=("Helvetica", 18), width=5, height=2,
                               command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row, column=column, padx=5, pady=5)

        self.scientific_mode = False

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif button_text == "C":
            self.result_var.set("")
        elif button_text == "√":
            try:
                result = math.sqrt(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif button_text == "^":
            self.result_var.set(self.result_var.get() + "**")
        elif button_text == "π":
            self.result_var.set(math.pi)
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button_text)

    def toggle_scientific_mode(self):
        if self.scientific_mode:
            self.scientific_mode = False
            self.root.geometry("400x400")
        else:
            self.scientific_mode = True
            self.root.geometry("600x400")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


