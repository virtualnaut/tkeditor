# Generate Default Properties

ROOT_WIDTH = 500
ROOT_HEIGHT = 400

def gen(widget):
    properties = []
    
    if widget == "ttk.Button":
        properties = ["width = $NULL$", "text = \"Button\""]
    elif widget == "ttk.Checkbutton":
        properties = ["text = \"Checkbutton\""]

    return properties

def root_methods():
    methods = {}
    
    methods['title'] = "Untitled"
    methods['resizable'] = [False, False]
    
    return methods

