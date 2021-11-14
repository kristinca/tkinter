import tkinter as tk
from tkinter import ttk


class FrameOne(tk.Frame):
    """The first frame"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.text = tk.StringVar()
        self.start_text = tk.StringVar()
        self.start_text.set("Frame No.1")

        text_label = ttk.Label(self, text=" Text : ")
        text_entry = ttk.Entry(self, textvariable=self.text)

        change_button = ttk.Button(self, text=' Change ', command=self.on_change)

        other_label = ttk.Label(self, textvariable=self.start_text, font=('TkDefaultFont', 24),
                              wraplength=400)

        text_label.grid(row=0, column=0, sticky=tk.W)
        text_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        change_button.grid(row=0, column=2, sticky=tk.E)
        other_label.grid(row=1, column=0, columnspan=3)

        self.columnconfigure(1, weight=1)

    def on_change(self):
        if self.text.get().strip():
            self.start_text.set(self.text.get())
        else:
            self.start_text.set("Frame No.1")


class MyApp(tk.Tk):
    """the app"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("A very simple app")
        self.geometry("400x400")
        self.resizable(width=True, height=True)
        FrameOne(self).grid(sticky=(tk.W + tk.E + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
