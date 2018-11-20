# Python Builder
# 06/11/18
# This will be used to generate the actual code for the user

import time_tools as tt

def generate_template(proj_name, proj_comments, proj_author, identifiers, data):
    
    content = ""

    # --Generate comments for the top of the file--
    content += "# " + proj_name
    content += "# " + tt.short_date + "/n"
    content += "# " + proj_author + "/n"
    content += "# Generated with tkEditor\n\n"

    # --Generate the classes--
    for identifier in identifiers:
        content += generate_class()

def widget_translate(data):
    # Data should be a list of the format found in "./data_spec.txt".

    # This will be where all of the translated code will go:
    translated = []
    
    for widget in data:
        # --Translate the widget's instantiation--
        # Assign to a variable
        instantiation = widget[1] + " = " + widget[0] + "(" + widget[2]

        # Put in the properties as arguments to the widget's constructor
        for widget_property in widget[5]:
            instantiation += ", " + widget_property

        instantiation += ")\n"

        # --Translate the widget's .place() call--
        place = widget[1] + ".place(" + widget[3] + ", " + widget[4] + ")\n\n"

        
        # --Translate the widget's called methods--
        methods = ""
        
        for method in widget[6]:
            methods += widget[1] + "." + method + "\n\n"

        # --Translate the widget's bindings--
        bindings = ""

        for binding in widget[7]:
            bindings += widget[1] + ".bind(" + binding + ")\n"

        total = instantiation + place + methods + bindings

        translated += [total]

    return translated

def root_translate(data):
    # Data should be a list of the format found in "./root_spec.txt".

    # This will be where all of the translated code will go:
    translated = []
    identifier = data[1]

    # --Translate the instantiation of the root window--
    instantiation = ""

    instantiation += identifier + " = " + data[0] + "()\n\n"

    # --Translate the methods--
    methods = ""

    for method in data[2]:
        methods += identifier + "." + method + "\n"

    # --Translate the bindings--
    bindings = ""

    for binding in data[3]:
        bindings += identifier + ".bind(" + binding + ")\n"

    # --Translate the protocols--
    protocols = ""

    for protocol in data[4]:
        protocols += identifier + ".protocol(" + protocol + ")\n"

    translated = instantiation + methods + bindings + protocols

    return translated
    
def generate_class(class_ident, root_data, widg_data):
    class_text = ""
    root_identifier = root_data[1]

    # This variable contains a single indent (4 spaces)
    i = "   "

    # --Generate the class' declaration--
    class_text += "class " + class_ident + ":\n"

    # --If implemented, control variables should go here--

    # --Root instantiation--
    class_text += i + "# Set up the window"
    class_text += i + root_translate(root_data)

    # --Set up image resources--

    # --Instantiate widgets--
    class_text += i + "# Set up widgets"
    class_text += i + widget_translate(widg_data)

    # --Start mainloop--
    class_text += i + root_identifier + ".mainloop()"

    return class_text

print(generate(["tk.Tk", "root", [], ["<Button-1>, dummyI"], ["\"WM_DELETE_WINDOW\", dummyII"]]))
