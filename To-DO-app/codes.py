import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=(0, 5))
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.listbox = tk.Listbox(root, width=45, height=10)
        self.listbox.pack(padx=10, pady=(0, 10))

        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_task)
        self.delete_button.pack(pady=(0, 5))

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            for i in reversed(selected):
                self.listbox.delete(i)
                del self.tasks[i]
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()