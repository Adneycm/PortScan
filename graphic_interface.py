import tkinter as tk
from tkinter import scrolledtext

class GraphicInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.title = "Port Scanner"
        self.window_size = "400x300"
        self.entry_host = None
        self.entry_port = None
        self.output = None


    def create_interface(self, command):
        self.window.title(self.title)
        self.window.geometry(self.window_size)

        label_host = tk.Label(self.window, text="Host:")
        label_host.pack()
        self.entry_host = tk.Entry(self.window)
        self.entry_host.pack()

        label_port = tk.Label(self.window, text="Ports (ex: 1-100):")
        label_port.pack()
        self.entry_port = tk.Entry(self.window)
        self.entry_port.pack()

        scan_button = tk.Button(self.window, text="Scan", command=command)
        scan_button.pack()

        self.output = scrolledtext.ScrolledText(self.window, width=40, height=10)
        self.output.pack()

        self.window.mainloop()