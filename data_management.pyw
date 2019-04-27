import general_tools as gt
import code_builder as cb
import defaults, keyword

class IdentifierUsed(Exception):
    pass

class PropertyError(Exception):
    pass

class data_manager:
    def __init__(self, win_type, root_identifier):
        self.widgets = []
        self.images = {}

        # Dictionary of index in self.widgets where a certain widget is stored
        # identifier : index
        self.location = {}
        
        self.root = [win_type, root_identifier, defaults.ROOT_WIDTH, defaults.ROOT_HEIGHT, 
                     [],
                     [defaults.root_methods()],
                     []]
        
        # Only update the root window when it is needed
        self.root_update_required = False

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
        strs = {"class": 0, "width": 2, "height": 3, "properties": 4, "methods": 5, "bindings": 6}
        
        self.root[strs[part]] = value
        
    def edit_root_method(self, method, value):
        self.root[5][0][method] = value

    def edit_widget(self, widget_identifier, part, value):
        # Edit the widget data of the widget using identifier 'widget_identifier'
        strs = {"class": 0, "master": 2, "x": 3, "y": 4, "properties": 5, "methods": 6, "bindings": 7}
        
        if (part == "x" or part == "y"):
            value = part+"="+str(value)

        if (part != "identifier") and (part != "properties") and (part != "methods"):
            accepted = self.__data_verif(part, value)

            if not accepted:
                self.widgets[self.location[widget_identifier]][strs[part]] = accepted
            else:
                self.widgets[self.location[widget_identifier]][strs[part]] = value


        else:
            if part == "identifier":
                self.widgets[self.location[widget_identifier]][1] = value
                self.location[value] = self.location.pop(widget_identifier)

            elif part == "properties":
                # If a property is being changed, change only the property that is supplied,
                #   and keep all the others.
                value = value[0]
                
                index = gt.property_find(self.widgets[self.location[widget_identifier]][5], value)
                self.widgets[self.location[widget_identifier]][5][index] = value


    def add_widget(self, widget_class, widget_identifier, parent,
                   x = 5, y = 5, properties = [], methods = [{}],
                   bindings = []):

        # Add a new widget to self.widgets
        if self.__verify_widget(widget_identifier):
            self.widgets += [[widget_class, widget_identifier, parent, "x=" + str(x), "y=" + str(y),
                              properties, methods, bindings]]

            self.location[widget_identifier] = len(self.widgets) - 1
        else:
            raise IdentifierUsed("A widget using that identifier already exists.")

    def change_identifier(self, old_identifier, new_identifier):
        # Update the location dict
        here = self.location.pop(old_identifier)
        self.location[new_identifier] = here

        # Update the actual data
        self.widgets[self.location[new_identifier]][1] = new_identifier
        
    def validate_identifier(self, identifier):
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        alphabet = []
        for ii in range(ord("a"), ord("z")):
            alphabet += [chr(ii)]
            
        valid_chars = digits + alphabet + ["_"]
        
        if (identifier in self.location.keys()) or (identifier == "$ROOT$") :
            return [False, 0]
        
        if keyword.iskeyword(identifier):
            return [False, 1]
        
        if identifier == "":
            return [False, 4]        
        
        if identifier[0] in digits:
            return [False, 2]
        
        for char in identifier:
            if char not in valid_chars:
                return [False, 3]
            
        return [True]
    
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

    def tabulate(self, widget):
        # All widgets must have:
        # - x coord
        # - y coord
        # - identifier
        # - parent

        data = self.widgets[self.location[widget]]

        props = {}
        props["Identifier"] = data[1]
        
        if type(data[3]) == str:
            props["X-Coord"] = (str(data[3]).replace(" ",""))[2:]
        else:
            props["X-Coord"] = data[3]

        if type(data[4]) == str:
            props["Y-Coord"] = (str(data[4]).replace(" ",""))[2:]
        else:
            props["Y-Coord"] = data[4]
            
        #props["Parent"] = ...
        props.update(gt.keyword_convert(data[5]))

        return props

    def root_tabulate(self):

        data = self.root
        
        props = {}
        props["Width"] = data[2]
        props["Height"] = data[3]

        props.update(gt.keyword_convert(data[4]))

        return props
"""        
def generate(root, widgets):
    # This function is called by the export method in ui.menu_ui
    # It returns the python code that generates the UI as a string.
    
    all_data = [root, widgets]
    return cb.generate_class(all_data)
"""