# Editor Interface

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

import data_management as data
import widgets as widg
import general_tools as gt
import defaults
import code_builder as cb

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
        self.root.resizable(False, False)
        
        #self.root.iconbitmap()         # Window's icon
        self.root.title("Untitled")     # The title of the window

        # Set up deselection
        self.root.bind("<Button-1>", self.__possible_selection)
        self.root.bind("<ButtonRelease-1>", self.__coord_upd)

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
            
        # Redraw the root window
        new_width = self.widget_manager.root[2]
        new_height = self.widget_manager.root[3]
             
        self.root.geometry(str(new_width) + "x" + str(new_height))

    def ui_supply(self, ui):
        self.selection_ui = ui

    def change_identifier(self, old, new):
        val = self.disp_widg.pop(old)
        self.disp_widg[new] = val
            
    def __possible_selection(self, event):
        if event.widget == self.effect_canv:
            # User has deselected the widgets
            
            for key in self.disp_widg.keys():
                self.disp_widg[key].movement.deselect()

            self.selection_ui.root_select()
                
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
                    
    def selection_box_fix(self, identifier):
        self.disp_widg[identifier].movement.deselect()
        self.disp_widg[identifier].movement.select()

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

    def __update(self):
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
        self.root = False

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
        print(properties.keys())
        
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

    def root_select(self):
        self.title.config(text = self.widgets.root[0])
        self.sub.config(text = self.widgets.root[1])

        properties = self.widgets.root_tabulate()
        
        self.table.delete(*self.used_iids)
        
        self.used_iids = []

        for prop in properties.keys():
            self.table.insert("", "end", iid = prop, values = [prop, properties[prop]])
            self.used_iids += [prop]

        self.displaying = "$ROOT$"

    def start(self):
        self.root.mainloop()

    def __dbl_clk(self):
        if len(self.table.selection()) == 1:
            if self.displaying != "$ROOT$":
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
                    prompt = prompt_ui(*prompt_data)
                    
            else:
                selected = self.table.selection()[0]
                if selected == "Width":
                    prompt = prompt_ui("Single", "Width", "Please enter a width:")
                elif selected == "Height":
                    prompt = prompt_ui("Single", "Height", "Please enter a height:")
                
        value = prompt.result

        if value != None:
            if value[0] != False:
                if self.displaying != "$ROOT$":
                    if selected == "Identifier":
                        # Update subtitle
                        self.sub.config(text = str(value[1]))

                        # Update data
                        self.widgets.change_identifier(self.displaying, value[1])
                        self.display_ui.change_identifier(self.displaying, value[1])
                        self.displaying = value[1]
                        
                    elif selected == "X-Coord":
                        print(value[1])
                        self.widgets.edit_widget(self.displaying, "x", value[1])
                        self.display_ui.disp_widg[self.displaying].x = int(value[1])

                    elif selected == "Y-Coord":
                        print(value[1])
                        self.widgets.edit_widget(self.displaying, "y", value[1])
                        self.display_ui.disp_widg[self.displaying].y = int(value[1])

                    else:
                        self.widgets.edit_widget(self.displaying, "properties", [(selected + " = " + str(value[1]))])
                else:
                    warnings = 0
                    new_width = value[1]
                    new_height = value[1]
                    
                    if selected == "Width":
                        window_width = int(value[1])
                        window_height = int(self.widgets.root[3])
                    else:
                        window_height = int(value[1])
                        window_width = int(self.widgets.root[2])

                    warning = False
                    correctees = []
                    correct_coords = []
                    for key in self.display_ui.disp_widg.keys():
                        check_results = gt.coord_validate(self.display_ui.disp_widg[key].x, self.display_ui.disp_widg[key].y, window_width, window_height)
                        
                        if check_results[0] == True:
                            warning = True
                            
                        correctees += [key]
                        correct_coords += [check_results[1]]
                        
                    if warning:
                        wants_correction = messagebox.askyesno("Move Widgets?", "One or more widgets will be moved to keep them in the window\nAre you sure you want to continue?")
                    
                        if wants_correction:
                            for widget in range(len(correctees)):
                                print(correct_coords[widget][0])
                                self.widgets.edit_widget(correctees[widget], "x", correct_coords[widget][0])
                                self.display_ui.disp_widg[correctees[widget]].x = correct_coords[widget][0]
                                
                                self.widgets.edit_widget(correctees[widget], "y", correct_coords[widget][1])
                                self.display_ui.disp_widg[correctees[widget]].y = correct_coords[widget][1]
                                
                                self.widgets.edit_root("width", window_width)
                                self.widgets.edit_root("height", window_height)
                    else:
                        self.widgets.edit_root("width", window_width)
                        self.widgets.edit_root("height", window_height)
                    
        # Fully refresh the display
        if self.displaying == "$ROOT$":
            self.root_select()
        else:
            self.set_display(self.displaying)
            self.display_ui.selection_box_fix(self.displaying)
         
        print("REFRESHING")
        self.display_ui.refresh()
        
class menu_ui:
    def __init__(self, widget_manager):
        
        # Widget Manager, for export data
        self.widget_manager = widget_manager
        
        # Set Up Window
        self.root = tk.Toplevel()
        self.root.geometry("285x100")
        self.root.title("Menu")
        
        # Buttons
        
        imgs = [tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png"),
                tk.PhotoImage(file="./resources/widget.png")]
                
        bg_unhov = tk.PhotoImage(file = "./resources/bg_unhov.png")
        bg_hov = tk.PhotoImage(file = "./resources/bg_hov.png")
        
        # New UI
        bg_new = ttk.Label(self.root)
        btn_new = ttk.Label(self.root)
        
        bg_new.image = bg_unhov
        btn_new.image = imgs[0]
        
        bg_new.config(image = bg_unhov)
        
        bg_new.place(x=10,y=10)
        btn_new.place(x=14,y=14)
        
        btn_new.bind("<Enter>", lambda event: bg_new.config(image = bg_hov))
        btn_new.bind("<Leave>", lambda event: bg_new.config(image = bg_unhov))
        
        btn_new.config(image = imgs[0])

        # Export UI
        bg_exp = ttk.Label(self.root)
        btn_exp = ttk.Label(self.root)
        
        bg_exp.image = bg_unhov
        btn_exp.image = imgs[1]
        
        bg_exp.config(image = bg_unhov)
        
        bg_exp.place(x=100,y=10)
        btn_exp.place(x=104,y=14)
        
        btn_exp.bind("<Enter>", lambda event: bg_exp.config(image = bg_hov))
        btn_exp.bind("<Leave>", lambda event: bg_exp.config(image = bg_unhov))
        btn_exp.bind("<Button-1>", lambda event: self.__export())
        
        btn_exp.config(image = imgs[1])
        
        # Save UI
        bg_sav = ttk.Label(self.root)
        btn_sav = ttk.Label(self.root)
        
        bg_sav.image = bg_unhov
        btn_sav.image = imgs[2]
        
        bg_sav.config(image = bg_unhov)
        
        bg_sav.place(x=190,y=10)
        btn_sav.place(x=194,y=14)
        
        btn_sav.bind("<Enter>", lambda event: bg_sav.config(image = bg_hov))
        btn_sav.bind("<Leave>", lambda event: bg_sav.config(image = bg_unhov))
        
        btn_sav.config(image = imgs[2])
        
    def __save(self):
        pass
        
    def __export(self):
        prepped = gt.noneify(self.widget_manager.root, self.widget_manager.widgets)
        TEMPPATH = "./output/proto.py"
        py_stream = open(TEMPPATH, "w+")
        py_stream.write(cb.generate_class("ui", prepped[0], prepped[1]))
        py_stream.close()
        
    def __new(self):
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
