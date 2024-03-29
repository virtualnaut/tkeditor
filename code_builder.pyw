# Python Builder
# 06/11/18
# This will be used to generate the actual code for the user

import general_tools as gt

def generate_template(proj_name, proj_comments, proj_author, identifiers, data):
    
    content = ""

    # --Generate comments for the top of the file--
    content += "# " + proj_name
    content += "# " + gt.short_date() + "/n"
    content += "# " + proj_author + "/n"
    content += "# Generated with tkEditor\n\n"

    # --Generate the classes--
    for identifier in identifiers:
        content += generate_class()

def widget_translate(data):
    # Data should be a list of the format found in "./specs/data_spec.txt".

    # This will be where all of the translated code will go:
    translated = []
    
    for widget in data:
        # Store a reference if the widget has an image
        image = ""
        if "image" in gt.keyword_convert(widget[5]).keys():
            image += widget[2] + "." + widget[1] + "_img = " + gt.keyword_convert(widget[5])["image"] + "\n"
        
        # --Translate the widget's instantiation--
        # Assign to a variable
        instantiation = widget[1] + " = " + widget[0] + "(" + widget[2]

        # Put in the properties as arguments to the widget's constructor
        for widget_property in widget[5]:
            if not widget_property.replace(" ","").startswith("image="):
                instantiation += ", " + gt.quote_escape(widget_property)
            else:
                instantiation += ", image = " + widget[2] + "." + widget[1] + "_img"

        instantiation += ")\n"

        # --Translate the widget's .place() call--
        place = widget[1] + ".place(" + widget[3] + ", " + widget[4] + ")\n\n"

        
        # --Translate the widget's called methods--
        methods = ""
        
        for method in widget[6][0].keys():
            methods += widget[1] + "." + method + "(" + widget[6][0][method] + ")\n\n"

        # --Translate the widget's bindings--
        bindings = ""

        for binding in widget[7]:
            bindings += widget[1] + ".bind(" + binding + ")\n"

        total = image + instantiation + place + methods + bindings

        translated += [total]
    return translated

def root_translate(data):
    # Data should be a list of the format found in "./specs/root_spec.txt".

    # This will be where all of the translated code will go:
    translated = []
    identifier = data[1]

    # --Translate the instantiation of the root window--
    instantiation = ""

    instantiation += identifier + " = " + data[0] + "()\n\n"

    # --Translate the methods--
    methods = identifier + ".geometry('" + str(data[2]) + "x" + str(data[3]) + "')\n"
    
    for method in data[5][0].keys():
        methods += gt.method_assemble(identifier, method, data[5][0][method]) + "\n"
        
    """
    # --Translate the bindings--
    bindings = ""

    for binding in data[5]:
        bindings += identifier + ".bind(" + binding + ")\n"

    # --Translate the protocols--
    protocols = ""

    for protocol in data[6]:
        protocols += identifier + ".protocol(" + protocol + ")\n"

    translated = instantiation + methods + bindings + protocols + "\n"
    """
    
    translated = instantiation + methods + "\n"
    return translated
    
def generate_class(class_ident, root_data, widg_data):
    class_text = ""
    root_identifier = root_data[1]

    # This variable contains a single indent (4 spaces)
    i = "    "

    # --Generate the class' declaration--
    class_text += "class " + class_ident + ":\n"

    # --Generate the constructor's declaration--
    class_text += i + "def __init__(self):\n\n"

    # --If implemented, control variables should go here--

    # --Root instantiation--
    class_text += i + i + "# Set up the window\n"
    class_text += gt.indent(gt.indent(root_translate(root_data)))

    # --Set up image resources--

    # --Instantiate widgets--
    class_text += i + i + "# Set up widgets\n"
    class_text += gt.unlistify(gt.indent(gt.indent(widget_translate(widg_data))))

    # --Start mainloop--
    class_text += i + i + "# Start mainloop\n"
    class_text += i + i + root_identifier + ".mainloop()"

    return class_text

def python_build(proj_name, root, widgets):
    content = ""

    # --Generate comments for the top of the file--
    content += "# " + proj_name + "\n"
    content += "# " + gt.short_date() + "\n"
    content += "# Generated with tkEditor\n\n"

    content += "import tkinter as tk\n"
    content += "from tkinter import ttk\n\n"
    
    content += generate_class("ui", root, widgets)
    
    content += "\n\nx = ui()"
    
    return content

#print(generate_class("tester",["tk.Tk", "root", [], ["<Button-1>, dummyI"], ["\"WM_DELETE_WINDOW\", dummyII"]], ))
"""
print(generate_class("CLASS",
               ["tk.Tk", "root", ["geometry('500x500')", "title('Test Window')"], 
                                 [],
                                 []],
               [["ttk.Button", "btn_a", "root", "x = 50", "y = 50", ["text = 'Click Me'"],
                                                                   [],
                                                                   []]]))

print(gt.indent(widget_translate([["ttk.Button", "btn_a", "root", "x = 50", "y = 50", ["text = 'Click Me'"],
                                                                   [],
                                                                   []]]))[0])

"""