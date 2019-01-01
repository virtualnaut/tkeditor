# Generate Default Properties

def gen(widget):
    properties = []
    
    if widget == "ttk.Button":
        properties = ["text = \"Button\""]
    elif widget == "ttk.Checkbutton":
        properties = ["text = \"Checkbutton\""]

    return properties
