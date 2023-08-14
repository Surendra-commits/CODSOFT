import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TLabel", font=("Helvetica", 12), foreground="#333")

        self.style.configure("Add.TButton", font=("Helvetica", 12))
        self.style.map("Add.TButton", foreground=[('active', 'black')], background=[('active', 'green')])

        self.style.configure("Remove.TButton", font=("Helvetica", 12))
        self.style.map("Remove.TButton", foreground=[('active', 'black')], background=[('active', 'red')])

        self.style.configure("Update.TButton", font=("Helvetica", 12))
        self.style.map("Update.TButton", foreground=[('active', 'black')], background=[('active', 'orange')])

        self.style.configure("Exit.TButton", font=("Helvetica", 12))
        self.style.map("Exit.TButton", foreground=[('active', 'black')], background=[('active', '#8b0000')])

        self.task_label = ttk.Label(root, text="Task:")
        self.task_label.grid(row=0, column=0, padx=5, pady=5)

        self.task_entry = ttk.Entry(root, font=("Helvetica", 12), width=30)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task, style="Add.TButton")
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12), selectbackground="#0078d4",
                                       selectforeground="white")
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.remove_button = ttk.Button(root, text="Remove Task", command=self.remove_task, style="Remove.TButton")
        self.remove_button.grid(row=2, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(root, text="Update Task", command=self.update_task, style="Update.TButton")
        self.update_button.grid(row=2, column=1, padx=5, pady=5)

        self.exit_button = ttk.Button(root, text="Exit", command=root.quit, style="Exit.TButton")
        self.exit_button.grid(row=2, column=2, padx=5, pady=5)

        self.style.configure("TListbox", background="#f0f0f0", foreground="#333")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.tasks.remove(task)

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            updated_task = simpledialog.askstring("Update Task", "Enter updated task:", initialvalue=task)
            if updated_task:
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task)
                self.tasks[selected_task_index[0]] = updated_task


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

