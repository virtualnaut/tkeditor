import tkinter as tk
from tkinter import ttk

class mobiliser:
    def __init__(self, tkWidget):
        self.inner = tkWidget
        self.curr_x = self.inner.x
        self.curr_y = self.inner.y

        # Set up bindings
        self.inner.bind("<Button-1>", self.dummy)
        self.inner.bind("<ButtonRelease-1>", self.dummy)

        self.inner.master.bind("<B1-Motion>", self.__move)
        self.inner.bind("<B1-Motion>", self.dummy)

    def dummy(self, event):
        print(event)
        
    def __drag(self, event):
        grab_x = event.x
        grab_y = event.y

        print(str(self.curr_x + grab_x), str(self.curr_y + grab_y))
        self.inner.place(x = self.curr_x + grab_x, y = self.curr_y + grab_y)

    def __move(self, event):
        self.curr_x = event.x
        self.curr_y = event.y
        self.inner.place(x = self.curr_x, y = self.curr_y)

class mButton(ttk.Button):
    def __init__(self, parent, **kwargs):
        # Properties
        self.prop_dict = kwargs
        self.x = 0
        self.y = 0
        
        # Raise an error if an invalid keyword is given
        self.__kwarg_validate(kwargs)

        # Call ttk constructor for this widget
        super().__init__(parent, **kwargs)

        # Set up bindings and their commands
        self.movement = mobiliser(self)

    def __kwarg_validate(self, values):
        # If one of the arguments' keywords is not in 'valid', raise TypeError
        valid = ["width","height","text","command","image","cursor"]
        for arg in values.keys():
            if arg not in valid:
                raise TypeError("Invalid keyword argument: "+arg)

    def config(self, **kwargs):
        self.__kwarg_validate(kwargs)
        self.prop_dict.update(kwargs)
        super().config(**kwargs)

    def place(self, x, y):
        self.x = x
        self.y = y
        super().place(x = x, y = y)

def debug():
    r=tk.Tk()
    a={"text":"Hello"}
    b = mButton(r, text="Hello World")
    b.place(x=20,y=20)
    b.config(text = "TEST")
    r.mainloop()

debug()
