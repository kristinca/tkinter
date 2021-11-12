import tkinter as tk
from tkinter import ttk


class HelloView(tk.Frame):
    """A friendly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World of tkinter w/ classes! ^^")

        name_label = ttk.Label(self, text="Text: ")
        name_entry = ttk.Entry(self, textvariable=self.name)

        ch_button = ttk.Button(self, text="Change", command=self.on_change)

        hello_label = ttk.Label(self, textvariable=self.hello_string, font=("TkDefaultFont", 64),
                                wraplength=600)

        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)

        self.columnconfigure(1, weight=1)

    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set("Hello "+self.name.get())
        else:
            self.hello_string.set("Hello world!")


class MyApp(tk.Tk):
    """Hello World Main Application"""

    # we don't need a parent widget this time, since the Tk
    # object is the root window and has no parent

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter with classes")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        HelloView(self).grid(sticky=(tk.E+tk.W+tk.N+tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()