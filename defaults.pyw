# Generate Default Properties

ROOT_WIDTH = 500
ROOT_HEIGHT = 400

def gen(widget):
    properties = []
    
    if widget == "ttk.Button":
        properties = ["width = $NULL$", "text = \"Button\"", "takefocus = False", "cursor = $NULL$"]
    elif widget == "ttk.Checkbutton":
        properties = ["text = \"Checkbutton\"", "takefocus = False", "cursor = $NULL$"]
    elif widget == "ttk.Combobox":
        properties = ["values = $NULL$", "takefocus = False", "cursor = $NULL$"]
    elif widget == "ttk.Label":
        properties = ["text = \"Label\"", "image = $NULL$", "cursor = $NULL$"]
    elif widget == "ttk.Entry":
        properties = ["width = $NULL$", "justify = $NULL$", "cursor = $NULL$"]
    elif widget == "ttk.Progressbar":
        properties = ["length = $NULL$", "orient = \"horizontal\"", "maximum = $NULL$", "mode = \"determinate\"", "cursor = $NULL$"]

    return properties

def root_methods():
    methods = {}
    
    methods['title'] = "Untitled"
    methods['resizable'] = [False, False]
    
    return methods

