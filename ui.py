# Editor Interface

import tkinter as tk
from tkinter import ttk

# The window where widget arrangement etc. happens
class display_window:
    def __init__(self):

        # Instantiate the root window
        self.root = tk.Tk()

        # Set default values for the root window
        self.root.geometry("500x400")   # Size of the window
        #self.root.iconbitmap()         # Window's icon
        self.root.title("Untitled")     # The title of the window

        self.b = ttk.Button(self.root, text = "Button")
        self.b.pack()
        
        self.root.mainloop()

x = display_window()
