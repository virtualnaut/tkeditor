# Editor Interface

import tkinter as tk
from tkinter import ttk

import data_management as data
import widgets as widg
import general_tools as gt
import defaults

class base:
    def __init__(self):
        # Instantiate the root window
        self.root = tk.Tk()
    
        # Set default values for the root window
        self.root.geometry("500x400")   # Size of the window
    
        #self.root.iconbitmap()         # Window's icon
        self.root.title("Ufasfd")     # The title of the window
        
    def begin(self):
        self.root.mainloop()
        

# The window where widget arrangement etc. happens
class display_window:
    def __init__(self, widget_manager, selection_ui):

        #self.widgets = []
        self.disp_widg = {}
        self.widget_manager = widget_manager
        
        self.selection_ui = selection_ui

        # Instantiate the root window
        self.root = tk.Toplevel()

        # Set default values for the root window
        self.root.geometry("500x400")   # Size of the window
        
        #self.root.iconbitmap()         # Window's icon
        self.root.title("Untitled")     # The title of the window

        # Set up deselection
        #self.root.bind("<Button-1>", self.deselect)
        self.root.bind("<Button-1>", self.possible_selection)

        # Canvas where selection boxes etc will appear
        self.effect_canv = tk.Canvas(self.root, width = 500, height = 400)
        self.effect_canv.place(x = 0, y = 0)
        
        #self.root.mainloop()

    def refresh(self):
        # Delete the old widgets and update coords
        for key in self.disp_widg.keys():
            self.widget_manager.edit_widget(key, "x", self.disp_widg[key].x)
            self.widget_manager.edit_widget(key, "y", self.disp_widg[key].y)
            
            self.disp_widg[key].destroy()

        # Redraw the widgets as they were
        self.disp_widg = {}
        for widget in self.widget_manager.widgets:

            # Instantiate the widget
            self.disp_widg[widget[1]] = widg.movable(widget[0], self.root, self.effect_canv,
                                                     **gt.keyword_convert(widget[5]))

            # Put the widget in the correct place, removing the "x=" part and any spaces
            self.disp_widg[widget[1]].place(x = int((widget[3].replace(" ",""))[2:]),
                                            y = int((widget[4].replace(" ",""))[2:]))
            
        #self.root.mainloop()
            
    def possible_selection(self, event):
        if event.widget == self.effect_canv:
            # User has deselected the widgets
            
            for key in self.disp_widg.keys():
                self.disp_widg[key].movement.deselect()
                
        else:
            # User has selected a widget
            selected = []
            for key in self.disp_widg.keys():
                if self.disp_widg[key].movement.selected == True:
                    selected += [key]
                    
            for item in selected:
                self.selection_ui.set_display(key)
                    
                    

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
            
        #self.root.mainloop()

    def __add(self, calling_widget):
        self.widgets.add_widget(calling_widget, "widget_" + str(self.counter), self.widgets.root[1],
                                x = 5, y = 5, properties = defaults.gen(calling_widget))
        
        self.counter += 1
        self.display.refresh()

class selection_ui:
    def __init__(self, widget_manager):

        # Widget manager
        self.widgets = widget_manager

        # Instantiate the root window
        self.root = tk.Toplevel()

        # Set default values for the root window
        self.root.geometry("300x500")   # Size of the window
        
        #self.root.iconbitmap()         # Window's icon
        self.root.title("Selection")    # The title of the window

        # Stop the user being able to resize the window
        self.root.resizable(False, False)

        self.title = ttk.Label(self.root, text = "Nothing Selected", font = ("Arial Bold", 18))
        self.title.place(x = 5, y = 5)
        #self.title.config(text = "Hello")

        self.sub = ttk.Label(self.root, text = "Properties of selected widgets appear here")
        self.sub.place(x = 6, y = 40)

        lbl_props = ttk.Label(self.root, text = "Properties:", font = ("Arial Bold", 10))
        lbl_props.place(x = 6, y = 80)

        self.table = ttk.Treeview(self.root, height = 18, columns = ["Property", "Value"], show = "headings")
        self.table.place(x = 6, y = 105)
        
        self.table.heading("Property", text = "Property")
        self.table.column("Property", width = 143)
        
        self.table.heading("Value", text = "Value")
        self.table.column("Value", width = 143)        

        #self.root.mainloop()

    def set_display(self, identifier):
        self.title.config(text = self.widgets.widgets[self.widgets.location[identifier]][0])
        #self.title.config(text = "Hello")
        #self.title.place(x=3,y=2)
        
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
        
#d = data.data_manager("tk.Tk", "self.root")
#d.add_widget("ttk.Button", "self.btn", "self.root")
#x = selection_ui(d)
#x.set_display()