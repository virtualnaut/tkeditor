import tkinter as tk
from tkinter import ttk

class mobiliser:
    def __init__(self, tkWidget):
        self.inner = tkWidget
        self.grab = [None, None]

        # Set up bindings
        self.inner.bind("<B1-Motion>", self.__drag)
        self.inner.bind("<ButtonPress-1>", self.__click)
        self.inner.master.bind("<Button-1>", self.deselect)

    def dummy(self, event):
        print(event.__dict__)
        
    def __drag(self, event):
        grab_x = (self.inner.master.winfo_pointerx() - self.inner.master.winfo_rootx()) - self.grab[0]
        grab_y = (self.inner.master.winfo_pointery() - self.inner.master.winfo_rooty()) - self.grab[1]

        #print(str(self.curr_x + grab_x), str(self.curr_y + grab_y))
        self.inner.place(x = grab_x, y = grab_y)
        
    def __click(self, event):
        self.select()
        self.__grab(event)
            
    def __grab(self, event):
        self.grab[0] = event.x
        self.grab[1] = event.y
    
    def select(self):
        self.inner.config(style = self.inner.selected_style_name)
        
    def deselect(self, event):
        if event.widget != self.inner:
            self.inner.config(style = self.inner.style_name)
    

class mButton(ttk.Button):
    def __init__(self, parent, **kwargs):
        # Properties
        self.prop_dict = kwargs
        self.x = 0
        self.y = 0
        
        # Styling
        self.__select_style = ttk.Style()
        self.__select_style.configure("Selected.TButton", background = "orange")
        self.style_name = "TButton"
        self.selected_style_name = "Selected.TButton"
        
        # Raise an error if an invalid keyword is given
        self.__kwarg_validate(kwargs)

        # Call ttk constructor for this widget
        super().__init__(parent, **kwargs)

        # Set up bindings and their commands
        self.movement = mobiliser(self)

    def __kwarg_validate(self, values):
        # If one of the arguments' keywords is not in 'valid', raise TypeError
        valid = ["width","height","text","command","image","cursor", "style"]
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
    #s=ttk.Style()
    #s.configure("a.TButton", background = "red")
    #b=ttk.Button(r,text = "txt",style="a.TButton")
    #b.pack()
    r.mainloop()

debug()
