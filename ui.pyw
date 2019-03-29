# Editor Interface

import tkinter as tk
from tkinter import ttk

import data_management as data
import widgets as widg
import general_tools as gt

# The window where widget arrangement etc. happens
class display_window:
    def __init__(self, widget_manager):

        #self.widgets = []
        self.disp_widg = {}
        self.widget_manager = widget_manager

        # Instantiate the root window
        self.root = tk.Tk()

        # Set default values for the root window
        self.root.geometry("500x400")   # Size of the window
        
        #self.root.iconbitmap()         # Window's icon
        self.root.title("Untitled")     # The title of the window

        # Canvas where dotted selection boxes etc will appear
        self.canv = tk.Canvas(self.root, width = 500, height = 400)
        self.canv.place(x = 0, y = 0)

    def refresh(self):
        #self.widgets = []

        # Delete the old widgets
        for key in self.disp_widg.keys():
            self.disp_widg[key].destroy()

        self.disp_widg = {}

        for widget in self.widget_manager.widgets:

            self.disp_widg[widget[1]] = widg.movable(widget[0], self.root, **gt.keyword_convert(widget[5]))
            self.disp_widg[widget[1]].place(x = int((widget[3].replace(" ",""))[2:]), y = int((widget[4].replace(" ",""))[2:]))

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
    def __init__(self, widget_manager, display):

        # Widget manager
        self.widgets = widget_manager

        # Default identifier counter
        self.counter = 0

        # Display window
        self.display = display
        
        # Set up basic window
        self.root = tk.Toplevel()
        self.root.geometry("408x329")
    
        self.root.title("tkEditor - Add Widgets")
        
        self.root.resizable(False, False)

        # Set up buttons
        """
        imgs = [tk.PhotoImage(file="./resources/btn.png"),
                tk.PhotoImage(file="./resources/c_btn.png"),
                tk.PhotoImage(file="./resources/cmbo.png"),
                tk.PhotoImage(file="./resources/entr.png"),
                tk.PhotoImage(file="./resources/frame.png"),
                tk.PhotoImage(file="./resources/lbl.png"),
                tk.PhotoImage(file="./resources/lblframe.png"),
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
        imgs = [tk.PhotoImage(file="./resources/btn.png"),
                tk.PhotoImage(file="./resources/c_btn.png"),
                tk.PhotoImage(file="./resources/cmbo.png"),
                tk.PhotoImage(file="./resources/entr.png"),
                tk.PhotoImage(file="./resources/frame.png"),
                tk.PhotoImage(file="./resources/lbl.png"),
                tk.PhotoImage(file="./resources/lblframe.png"),
                tk.PhotoImage(file="./resources/prog.png"),
                tk.PhotoImage(file="./resources/r_btn.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png")]

        bg_unhov = tk.PhotoImage(file = "./resources/bg_unhov.png")
        bg_hov = tk.PhotoImage(file = "./resources/bg_hov.png")

        bgs = []
        btns = []

        order = ["ttk.Button", "ttk.Checkbutton", "ttk.Combobox", "ttk.Entry",
                 "ttk.Frame", "tk.Label", "tk.LabelFrame", "ttk.ProgressBar",
                 "ttk.Radiobutton", "ttk.Scale", "ttk.Separator",
                 "ttk.Treeview", "tk.Canvas", "tk.Listbox", "tk.Message",
                 "tk.OptionMenu", "tk.Spinbox", "tk.Text"]

        x = 5
        y = 5

        for img in range(len(imgs)):
            
            # Instantiate all of the image labels and add them to 'btns'
            bgs += [tk.Label(self.root, image = bg_unhov)]
            btns += [tk.Label(self.root, image = imgs[img])]

            # Put them all in the correct places (grid format)
            if (img % 5 == 0) and (img != 0):
                x = 5
                y += 80

            elif img != 0:
                x += 80

            bgs[img].place(x = x, y = y)
            btns[img].place(x = x+4, y = y+4)
            
            
        # Bind each button to the __add function, so that they add a widget to
        #   the display window when clicked.
        # Also set up button hovering
        for ii in range(len(btns)):
            btns[ii].bind("<Button-1>", lambda event, me = order[ii]: self.__add(me))
            
            btns[ii].bind("<Enter>", lambda event, ind = ii:
                          bgs[ind].config(image = bg_hov))
            
            btns[ii].bind("<Leave>", lambda event, ind = ii:
                          bgs[ind].config(image = bg_unhov))
            
        self.root.mainloop()

    def __add(self, calling_widget):
        self.widgets.add_widget(calling_widget, "widget_" + str(self.counter), self.widgets.root[1],
                                x = 5, y = 5)
        self.counter += 1
        self.display.refresh()


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
#x = add_ui(None)
#x=prompt_ui("Project Name","",None)
