# Editor Interface

import tkinter as tk
from tkinter import ttk

import data_management as data

# The window where widget arrangement etc. happens
class display_window:
    def __init__(self, widget_manager):

        self.widgets = []
        self.widget_manager = widget_manager

        # Instantiate the root window
        self.root = tk.Tk()

        # Set default values for the root window
        self.root.geometry("500x400")   # Size of the window
        
        #self.root.iconbitmap()         # Window's icon
        self.root.title("Untitled")     # The title of the window

    def refresh():
        self.widgets = []

        for widget in self.widget_manager.widgets:
            # FOR EACH WIDGET:
            # add list to self.widgets containing the MOVABLE WIDGET
            # TASKS
            # instantiate w/ parent
            # .place(x = x, y = y)
            # .config( ... )

            # REMEMBER MOVABLE WIDGETS!!
            # FIND AND COPY FILE

        

# The widget explorer
class tree_ui:
    def __init__(self, class_name):

        # Instantiate the root window
        self.root = tk.Tk()

        # Set default values for the root window
        self.root.geometry("300x500")   # Size of the window
        
        #self.root.iconbitmap()         # Window's icon
        self.root.title("Untitled - Widgets")     # The title of the window

        # Stop the user being able to resize the window
        self.root.resizable(False, False)

    def __update():
        pass

# The widget adder
class add_ui:
    def __init__(self, widget_manager):

        # Widget manager
        self.widgets = widget_manager

        # Default identifier counter
        self.counter = 0
        
        # Set up basic window
        self.root = tk.Toplevel()
        self.root.geometry("408x329")
    
        self.root.title("tkEditor - Add Widgets")
        
        self.root.resizable(False, False)

        # Set up buttons

        # Images must be 75x75
        """
        imgs = [tk.PhotoImage(file="./resources/btn.png"),
                tk.PhotoImage(file="./resources/c_btn.png"),
                tk.PhotoImage(file="./resources/cmbo.png"),
                tk.PhotoImage(file="./resources/entr.png"),
                tk.PhotoImage(file="./resources/frame.png"),
                tk.PhotoImage(file="./resources/lbl.png"),
                tk.PhotoImage(file="./resources/lbl_frame.png"),
                tk.PhotoImage(file="./resources/prog.png"),
                tk.PhotoImage(file="./resources/r_btn.png"),
                tk.PhotoImage(file="./resources/scale.png"),
                tk.PhotoImage(file="./resources/sep.png"),
                tk.PhotoImage(file="./resources/tree.png"),
                tk.PhotoImage(file="./resources/canv.png"),
                tk.PhotoImage(file="./resources/lst_bx.png"),
                tk.PhotoImage(file="./resources/msg.png"),
                tk.PhotoImage(file="./resources/optn.png"),
                tk.PhotoImage(file="./resources/spn_bx.png"),
                tk.PhotoImage(file="./resources/txt.png")]
        """
        imgs = [tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png")]
        
        btns = []

        order = ["ttk.Button", "ttk.Checkbutton", "ttk.Combobox", "ttk.Entry",
                 "ttk.Frame", "ttk.Label", "ttk.LabelFrame", "ttk.ProgressBar",
                 "ttk.Radiobutton", "ttk.Scale", "ttk.Separator",
                 "ttk.Treeview", "tk.Canvas", "tk.Listbox", "tk.Message",
                 "tk.OptionMenu", "tk.Spinbox", "tk.Text"]

        x = 5
        y = 5

        for img in range(len(imgs)):
            
            # Instantiate all of the image labels and add them to 'btns'
            btns += [ttk.Label(self.root, image = imgs[img])]

            # Put them all in the correct places (grid format)
            if (img % 5 == 0) and (img != 0):
                x = 5
                y += 80

            elif img != 0:
                x += 80

            btns[img].place(x = x,y = y)


        # Bind each button to the __add function, so that they add a widget to
        #   the display window when clicked.
        for ii in range(len(btns)):
            btns[ii].bind("<Button-1>", lambda event, me = order[ii]: self.__add(me))
            
        self.root.mainloop()

    def __add(self, calling_widget):
        self.widgets.add_widget(calling_widget, "widget_" + str(self.counter), self.widgets.root[1],
                                x = 5, y = 5)


class menu_ui():
    def __init__(self):
        pass

# UNFINISHED
#   This will be used to prompt user for text data.
class prompt_ui():
    def __init__(self, title, message, entry_width):
        # Set up basic window
        self.root = tk.Tk()
        self.root.geometry("408x329")
    
        self.root.title(str(title))
        
        self.root.resizable(False, False)

        self.root.mainloop()
        

"""
self.root.config(background = "#ffffff")

filemenu = tk.Menu(self.root, tearoff = 0)
filemenu.add_command(label = "Open File")

menubar = tk.Menu(self.root)
menubar.add_cascade(label = "File", menu = filemenu)
#menubar.add_command(label = "E")

self.root.config(menu = menubar)

self.root.mainloop()
"""
#x = add_ui()
#x=prompt_ui("Project Name","",None)
