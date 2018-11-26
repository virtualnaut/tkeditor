import tkinter as tk
from tkinter import ttk

class CLASS:
    # Set up the window
    root = tk.Tk()
    
    root.geometry('500x500')
    root.title('Test Window')
    
    # Set up widgets
    btn_a = ttk.Button(root, text = 'Click Me')
    btn_a.place(x = 50, y = 50)
    
    root.mainloop()

x = CLASS()
