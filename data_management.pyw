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
        strs = {"t":0,"m":2,"b":3,"p":4}

        if part != "i":
            try:
                self.widgets[self.location[widget_identifier]][strs[part]] = value
            except:
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

class tree_management:
    def __init__(self, tree):
        pass

    def __get_props(self, wi):
        pass
        
    def add_widget(self, widget_class, widget_identifier):
        pass

    def conf_widget(self):
        pass
"""
x = data_manager("tk.Tk", "self.r")
x.add_widget("ttk.Button", "self.b", "self.r", 223, 452, [], [], [])
print(x.location)
print(x.widgets)

x.edit_widget("self.b", "i", "b")
print(x.location)
print(x.widgets)
"""

x=data_manager("tk.Tk", "self.r")
x.add_widget("ttk.Button", "self.b", "self.r", 223, 452, [], [], [])
print(x.widgets)
