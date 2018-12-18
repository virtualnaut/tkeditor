import tkinter as tk
from tkinter import ttk

r = tk.Tk()
r.geometry("300x300")

t = ttk.Treeview(r, columns = ["a","b"])
t.place(x=5,y=5)

t.insert("", 0, iid = "i1", text = "Item1")
t.heading("a", text = "Name")

o = ttk.OptionMenu(r, "a","b")
o.place(x=0,y=0)
t.mainloop()
