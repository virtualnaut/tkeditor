class IdentifierUsed(Exception):
    pass

class PropertyError(Exception):
    pass

class data_manager:
    def __init__(self, win_type, root_identifier):
        self.widgets = []

        # Dictionary of index in self.widgets where a certain widget is stored
        # identifier : index
        self.location = {}
        
        self.root = [win_type, root_identifier, [], [], []]

    def __verify_widget(self, widget_identifier):
        # Check if the identifier is already used
        
        allowed = False

        try:
            self.location[widget_identifier]
        except KeyError:
            allowed = True

        if self.root[1] == widget_identifier:
            allowed = False
        
        return allowed

    def edit_root(self, part, value):
        # Edit the root data
        strs = {"t":0,"i":1,"m":2,"b":3,"p":4}

        try:
            self.root[strs[part]] = value
        except:
            raise PropertyError("That property doesn't exist.")

    def edit_widget(self, widget_identifier, part, value):
        # Edit the widget data of the widget using identifier 'widget_identifier'
        strs = {"class":0,"master":2,"x":3,"y":4,"properties":5,"methods":6,"bindings":7}

        if part != "identifier":
            try:
                accepted = self.__data_verif(part, value)
                
                if accepted != True:
                    self.widgets[self.location[widget_identifier]][strs[part]] = accepted
                else:
                    self.widgets[self.location[widget_identifier]][strs[part]] = value
            except:
                #import traceback
                #traceback.print_exc()
                raise PropertyError("That property doesn't exist.")
        else:
            self.widgets[self.location[widget_identifier]][1] = value
            self.location[value] = self.location.pop(widget_identifier)
        
    def add_widget(self, widget_class, widget_identifier, parent,
                   x = 0, y = 0, properties = [], methods = [],
                   bindings = []):

        # Add a new widget to self.widgets
        if self.__verify_widget(widget_identifier):
            self.widgets += [[widget_class, widget_identifier, parent, "x=" + str(x), "y=" + str(y),
                              properties, methods, bindings]]

            self.location[widget_identifier] = len(self.widgets) - 1
        else:
            raise IdentifierUsed("A widget using that identifier already exists.")

    def __data_verif(self, part, value):
        # Verify the data and fix minor errors
        orig = value
        if part == "class":
            allowed = ["ttk.Button", "ttk.Checkbutton", "ttk.Combobox", "ttk.Entry",
                       "tk.Label", "ttk.ProgressBar","ttk.Scale", "ttk.Separator",
                       "tk.Listbox","tk.OptionMenu", "tk.Spinbox", "tk.Text"]
            to_implement = ["ttk.Frame", "tk.LabelFrame", "ttk.Radiobutton", "ttk.Treeview",
                            "tk.Canvas", "tk.Message"]
            if value not in allowed:
                raise ValueError("Class \""+value+"\" is not supported.")
            
        elif part == "master":
            pass
        
        elif part == "x":
            if str(value)[:2] != "x=":
                value = "x=" + str(value)
            try:
                int(str(value)[2:])
            except ValueError:
                raise(ValueError("Invalid x coordinate"))
            
        elif part == "y":
            if str(value)[:2] != "y=":
                value = "y=" + str(value)
            try:
                int(str(value)[2:])
            except ValueError:
                raise(ValueError("Invalid y coordinate"))

        if orig == value:
            return True
        else:
            return value
"""      
class selection_manager:
    def __init__(self, select_ui):
        self.states = {}
    
    def modify(self, indentifier, state):
        if type(state) == bool:
            self.states[identifier] = state
        else:
            raise ValueError("Argument 'state' must be a bool.")
        
    def nudge(self):
"""     