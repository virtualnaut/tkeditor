import tkinter as tk
from tkinter import ttk
import time

class mobiliser:
    def __init__(self, tkWidget, effects, double_clk = False):
        
        # The actual tkinter widget
        self.inner = tkWidget

        self.grab = [None, None]        # Where on the widget the user has pressed btn1 down
        self.selected = False           # Is the widget selected?
        self.double_clk = double_clk    # Can the widget be altered via a double click?
        self.effects = effects          # Canvas where selection effects are displayed

        # Set up bindings
        self.inner.bind("<B1-Motion>", lambda event: self.__drag())
        self.inner.bind("<ButtonPress-1>", self.__grab)
        self.inner.bind("<ButtonRelease-1>", lambda event: self.select_effect())

        if self.double_clk:
            self.inner.bind("<Double-Button-1>", lambda event: self.enable())
        
    def __drag(self):
        # Calculate the new location of the widget relative the the root window's origin
        new_loc_x = (self.inner.master.winfo_pointerx() - self.inner.master.winfo_rootx()) - self.grab[0]
        new_loc_y = (self.inner.master.winfo_pointery() - self.inner.master.winfo_rooty()) - self.grab[1]

        # Set the properties of the inner widget to match
        self.inner.x = new_loc_x
        self.inner.y = new_loc_y

        # Update the display
        self.inner.place(x = new_loc_x, y = new_loc_y)

        #self.deselect()
        self.effects.delete("all")
        if self.double_clk:
            self.inner.state(["disabled"])

    def __grab(self, event):
        # Store the location that the widget is grabbed and select the widget
        self.select()
        
        self.grab[0] = event.x
        self.grab[1] = event.y
    
    def select(self):
        # Select the widget and display selection effect
        self.select_effect()
        self.selected = True

    def deselect(self):
        # Remove all effects and deselect
        self.effects.delete("all")
        self.selected = False

        # If the widget can be double clicked, disable the widget
        if self.double_clk:
            self.inner.state(["disabled"])

    def select_effect(self):
        self.effects.delete("all")
        self.effects.create_rectangle(self.inner.x-4, self.inner.y-4,
                                     (self.inner.x + self.inner.winfo_reqwidth()+4),
                                     (self.inner.y + self.inner.winfo_reqheight())+4,
                                     dash = (3,3), outline = "#00a3ff") 
        
    def enable(self):
        self.inner.state(["!disabled"])
    
class mButton(ttk.Button):
    def __init__(self, parent, effects, **kwargs):
        # Properties
        self.prop_dict = kwargs
        self.x = 0
        self.y = 0
        
        # Raise an error if an invalid keyword is given
        self.__kwarg_validate(kwargs)

        # Call ttk constructor for this widget
        super().__init__(parent, **kwargs)

        # Set up bindings and their commands
        self.movement = mobiliser(self, effects)

    def __kwarg_validate(self, values):
        # If one of the arguments' keywords is not in 'valid', raise TypeError
        valid = ["width","height","text","command","image","cursor", "style","takefocus"]
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

class mCheckbutton(ttk.Checkbutton):
    def __init__(self, parent, effects, **kwargs):
        # Properties
        self.prop_dict = kwargs
        self.x = 0
        self.y = 0
        
        # Raise an error if an invalid keyword is given
        self.__kwarg_validate(kwargs)

        # Call ttk constructor for this widget
        super().__init__(parent, **kwargs)

        # Set up bindings and their commands
        self.movement = mobiliser(self, effects, double_clk = True)
        
        self.invoke()
        self.state(["disabled"])
        

    def __kwarg_validate(self, values):
        # If one of the arguments' keywords is not in 'valid', raise TypeError
        valid = ["width","text","image","command","cursor", "takefocus", "style"]
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

class mCombobox(ttk.Combobox):
    def __init__(self, parent, effects, **kwargs):
        # Properties
        self.prop_dict = kwargs
        self.x = 0
        self.y = 0
        
        # Raise an error if an invalid keyword is given
        self.__kwarg_validate(kwargs)

        # Call ttk constructor for this widget
        super().__init__(parent, **kwargs)

        # Set up bindings and their commands
        self.movement = mobiliser(self, effects, double_clk = True)

        self.state(["disabled"])

    def __kwarg_validate(self, values):
        # If one of the arguments' keywords is not in 'valid', raise TypeError
        valid = ["width","height","values","postcommand","justify", "takefocus", "cursor", "style"]
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

class mLabel(ttk.Label):
    def __init__(self, parent, effects, **kwargs):
        # Properties
        self.prop_dict = kwargs
        self.x = 0
        self.y = 0
        
        # Raise an error if an invalid keyword is given
        self.__kwarg_validate(kwargs)

        # Call ttk constructor for this widget
        super().__init__(parent, **kwargs)

        # Set up bindings and their commands
        self.movement = mobiliser(self, effects)

    def __kwarg_validate(self, values):
        # If one of the arguments' keywords is not in 'valid', raise TypeError
        valid = ["width", "text", "image", "cursor", "justify"]
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
        
class mEntry(ttk.Entry):
    def __init__(self, parent, effects, **kwargs):
        # Properties
        self.prop_dict = kwargs
        self.x = 0
        self.y = 0
        
        # Raise an error if an invalid keyword is given
        self.__kwarg_validate(kwargs)

        # Call ttk constructor for this widget
        super().__init__(parent, **kwargs)

        # Set up bindings and their commands
        self.movement = mobiliser(self, effects)

    def __kwarg_validate(self, values):
        # If one of the arguments' keywords is not in 'valid', raise TypeError
        valid = ["width", "text", "image", "cursor", "justify", "takefocus"]
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
        
class mProgressbar(ttk.Progressbar):
    def __init__(self, parent, effects, **kwargs):
        # Properties
        self.prop_dict = kwargs
        self.x = 0
        self.y = 0
        
        # Raise an error if an invalid keyword is given
        self.__kwarg_validate(kwargs)

        # Call ttk constructor for this widget
        super().__init__(parent, **kwargs)

        # Set up bindings and their commands
        self.movement = mobiliser(self, effects)

    def __kwarg_validate(self, values):
        # If one of the arguments' keywords is not in 'valid', raise TypeError
        valid = ["length", "maximum", "orient", "cursor", "mode", "takefocus"]
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

def movable(widget_type, parent, effects, **kwargs):
    if widget_type == "ttk.Button":
        return mButton(parent, effects, **kwargs)
    if widget_type == "ttk.Checkbutton":
        return mCheckbutton(parent, effects, **kwargs)
    if widget_type == "ttk.Combobox":
        return mCombobox(parent, effects, **kwargs)
    if widget_type == "ttk.Label":
        return mLabel(parent, effects, **kwargs)
    if widget_type == "ttk.Entry":
        return mEntry(parent, effects, **kwargs)
    if widget_type == "ttk.Progressbar":
        return mProgressbar(parent, effects, **kwargs)

def debug():
    r=tk.Tk()
    a={"text":"Hello"}
    #b = mButton(r, text="Hello World")
    #b.place(x=20,y=20)
    #b.config(text = "TEST")
    #s=ttk.Style()
    #s.configure("a.TButton", background = "red")
    #b=ttk.Button(r,text = "txt",style="a.TButton")
    #b.pack()
    c=mCombobox(r, values=["a","b"])
    c.place(x=10,y=10)
    r.mainloop()

#debug()
