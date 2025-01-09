import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#f0f8ff")  

        self.expression = ""

       
        self.entry = tk.Entry(
            root, font=("Helvetica", 24), bg="#ffffff", fg="#000000", bd=0, justify="right"
        )
        self.entry.pack(pady=20, padx=10, ipady=10, fill="x")

        
        self.buttons_frame = tk.Frame(root, bg="#f0f8ff")
        self.buttons_frame.pack(pady=10)

        
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0, 4) 
        ]

        
        for text, row, col, *span in buttons:
            colspan = span[0] if span else 1
            button = tk.Button(
                self.buttons_frame,
                text=text,
                font=("Helvetica", 18),
                bg="orange",  
                fg="#ffffff",
                bd=0,
                width=10 if colspan > 1 else 5,
                height=2,
                relief="flat",
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
            button.bind("<Enter>", lambda e, b=button: b.configure(bg="#87ceeb"))  
            button.bind("<Leave>", lambda e, b=button: b.configure(bg="#4682b4"))  

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
        else:
            self.expression += char
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
