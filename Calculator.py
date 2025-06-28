import tkinter as tk
import winsound  # For sound on Windows (optional)

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x500")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        self._create_widgets()
        self._bind_keys()

    def _create_widgets(self):
        self.expr = tk.StringVar()
        self.display = tk.Entry(self, textvariable=self.expr, font=('Segoe UI', 24),
                                justify='right', bd=10, relief='sunken', bg='white')
        self.display.pack(fill='x', padx=10, pady=20)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]

        for row in buttons:
            frame = tk.Frame(self, bg="#f0f0f0")
            frame.pack(expand=True, fill='both', padx=10, pady=2)
            for label in row:
                btn = tk.Button(
                    frame, text=label,
                    font=('Segoe UI', 16, 'bold'),
                    padx=10, pady=10, bd=1,
                    bg="#ffffff", fg="#000000",
                    activebackground="#d0d0d0",
                    relief="raised",
                    command=lambda l=label: self.on_button(l)
                )
                btn.pack(side='left', expand=True, fill='both', padx=2, pady=2)

    def on_button(self, label):
        try:
            winsound.Beep(800, 50)  # Comment this if not on Windows
        except:
            pass

        txt = self.expr.get()

        if label == 'C':
            self.expr.set('')
        elif label == '=':
            try:
                result = str(eval(txt))
                self.expr.set(result)
            except:
                self.expr.set("Error")
        else:
            self.expr.set(txt + label)

    def _bind_keys(self):
        for key in '0123456789.+-*/':
            self.bind(key, lambda e, k=key: self.on_button(k))
        self.bind('<Return>', lambda e: self.on_button('='))
        self.bind('<BackSpace>', lambda e: self.expr.set(self.expr.get()[:-1]))
        self.bind('<Escape>', lambda e: self.expr.set(''))

if __name__ == "__main__":
    Calculator().mainloop()
