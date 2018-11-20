import tkinter as tk
from tkinter import ttk

r = tk.Tk()
r.geometry("500x500")

t = ttk.Treeview(r, height = 200)
t.pack()

t.insert("",0,"a", text = "Hello")
r.mainloop()
