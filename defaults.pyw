# Generate Default Properties

def gen(widget):
    properties = []
    
    if widget == "ttk.Button":
        properties = ["width = $NULL$", "text = \"Button\""]
    elif widget == "ttk.Checkbutton":
        properties = ["text = \"Checkbutton\""]

    return properties
