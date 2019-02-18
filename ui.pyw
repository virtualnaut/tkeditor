# Editor Interface

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

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
    def __init__(self, widget_manager):

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
        self.root.bind("<Button-1>", self.__possible_selection)
        self.root.bind("<ButtonRelease-1>", self.__coord_upd)

        # Canvas where selection boxes etc will appear
        self.effect_canv = tk.Canvas(self.root, width = 500, height = 400)
        self.effect_canv.place(x = 0, y = 0)
        
        #self.root.mainloop()

    def refresh(self):
        print(self.disp_widg.keys())
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

    def ui_supply(self, ui):
        self.selection_ui = ui

    def change_identifier(self, old, new):
        val = self.disp_widg.pop(old)
        self.disp_widg[new] = val
            
    def __possible_selection(self, event):
        if event.widget == self.effect_canv:
            # User has deselected the widgets

            self.selection_ui.revert()
            
            for key in self.disp_widg.keys():
                self.disp_widg[key].movement.deselect()
                
        else:
            # User has selected a widget
            for key in self.disp_widg.keys():
                if event.widget == self.disp_widg[key].movement.inner:
                    self.selection_ui.set_display(key)

    def __coord_upd(self, event):
        for ident in self.disp_widg.keys():
            self.widget_manager.edit_widget(ident, "x", self.disp_widg[ident].x)
            self.widget_manager.edit_widget(ident, "y", self.disp_widg[ident].y)

        if event.widget != self.effect_canv:
            for key in self.disp_widg.keys():
                if self.disp_widg[key].movement.inner == event.widget:
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

            btns[img].image = imgs[img]

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

        # Current Display
        self.displaying = None

        # Needs Refresh?
        self.req_update = False

        # Instantiate the root window
        self.root = tk.Tk()

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
        
        self.used_iids = []

        self.table = ttk.Treeview(self.root, height = 18, columns = ["Property", "Value"], show = "headings")
        self.table.place(x = 6, y = 105)
        
        self.table.heading("Property", text = "Property")
        self.table.column("Property", width = 143)
        
        self.table.heading("Value", text = "Value")
        self.table.column("Value", width = 143)

        self.root.bind("<Return>", lambda event: self.__dbl_clk())
        self.root.bind("<Double-Button-1>", lambda event: self.__dbl_clk())
        #self.root.mainloop()

    def ui_supply(self, ui):
        self.display_ui = ui

    def set_display(self, identifier):
        self.title.config(text = self.widgets.widgets[self.widgets.location[identifier]][0])
        self.sub.config(text = self.widgets.widgets[self.widgets.location[identifier]][1])
        
        properties = self.widgets.tabulate(identifier)
        
        self.table.delete(*self.used_iids)
        
        self.used_iids = []
        
        for prop in properties.keys():
            self.table.insert("", "end", iid = prop, values = [prop, properties[prop]])
            self.used_iids += [prop]

        self.displaying = identifier

    def revert(self):
        self.title.config(text = "Nothing Selected")
        self.sub.config(text = "Properties of selected widgets appear here")
        self.table.delete(*self.used_iids)
        self.used_iids = []
        self.displaying = None

    def start(self):
        self.root.mainloop()

    def __dbl_clk(self):
        if len(self.table.selection()) == 1:

            selected = self.table.selection()[0]

            # Changing X Coord
            if selected == "X-Coord":
                prompt = prompt_ui("Single", "X Coordinate", "Please enter a value:")

            # Changing Y Coord
            elif selected == "Y-Coord":
                prompt = prompt_ui("Single", "Y Coordinate", "Please enter a value:")

            # Changing Identifier
            elif selected == "Identifier":
                prompt = prompt_ui("Single", "Identifier", "Please enter a new identifier:")

            # Changing a Property
            else:
                prompt_data = gt.prompt_type(selected)
                prompt = prompt_ui(prompt_data[0], prompt_data[1], prompt_data[2])
                
        value = prompt.result

        if value != None:
            if value[0] != False:
                if selected == "Identifier":
                    # Update subtitle
                    self.sub.config(text = str(value[1]))

                    # Update data
                    self.widgets.change_identifier(self.displaying, value[1])
                    self.display_ui.change_identifier(self.displaying, value[1])
                    self.displaying = value[1]
                    
                elif selected == "X-Coord":
                    pass

                elif selected == "Y-Coord":
                    pass

                else:
                    self.widgets.edit_widget(self.displaying, "properties", [(selected + " = " + str(value[1]))])
        

        # Fully refresh the display
        self.set_display(self.displaying)
        
        self.display_ui.refresh()
        
class menu_ui:
    def __init__(self):
        pass

# This will be used to prompt user for text data.
class prompt_ui():
    def __init__(self, window_type, title, message):
        allowed_types = ["Single"]
        self.window_type = window_type
        self.result = None
        
        if window_type in allowed_types:
            # Master window
            self.root = tk.Toplevel()
            self.root.resizable(False, False)

            # A window for entering a single value e.g. string for text, or a number for coords
            if window_type == "Single":
                self.root.geometry("300x90")
                self.root.title(str(title))

                self.message = ttk.Label(self.root, text = str(message))
                self.message.place(x = 5, y = 5)

                # Buttons
                self.input = ttk.Entry(self.root, width = 47)
                self.input.place(x = 5, y = 30)

                self.accept = ttk.Button(self.root, text = "Accept", command = self.__accept)
                self.accept.place(x = 220, y = 60)

                self.accept = ttk.Button(self.root, text = "Cancel", command = self.root.destroy)
                self.accept.place(x = 140, y = 60)

                self.default = ttk.Button(self.root, text = "Default")
                self.default.place(x = 60, y = 60)

                # Bindings
                self.root.bind("<Return>", lambda event: self.__accept())
                self.root.bind("<Escape>", lambda event: self.__cancel())

            elif window_type == "Explorer":
                return filedialog.askopenfilename(initialdir = "C:/", title = "Please Select an Image", filetypes = (("PNG files", "*.png"), ("JPG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("All types", "*.*")))

            self.root.mainloop()
        else:
            raise ValueError("Please specify a valid type of window.")
        # Set up basic window
        
        
    def __accept(self):
        if self.window_type == "Single":
            value = self.input.get()
            self.root.quit()
            self.root.destroy()
            self.result = [True, value]

    def __cancel(self):
        self.root.quit()
        self.root.destroy()
        self.result = [False, None]

#d = data.data_manager("tk.Tk", "self.root")
#d.add_widget("ttk.Button", "self.btn", "self.root")
#x = selection_ui(d)
#x.set_display()

#prompt_ui("Single", "New Text", "Please enter a string:")
