# GENERAL TOOLS
# 12/11/18
# This module contains functions that are useful throughout the whole
#    project.

import time
from tkinter import PhotoImage

# This will be used to read the CSV file which contains the properties
#   and names of the widgets.

def csv_parse(path, delimiter = ","):
    # 'path' is the location of the txt/csv file in the file system.
    # 'delimiter' is the character that has been used in the file
    #   to separate the values, default is a comma for csv files.

    # --Open the file--
    READ = "r"
    file = open(path, READ)

    # --Read the data from the file, line by line--
    last_line = None
    lines = []

    # Keep going until there is no more data.
    while last_line != "":
        last_line = file.readline()

        # If there is data, append it to the 'lines' list.
        if last_line != "":
            lines += [last_line]

    # --Reading is finished, so close the file--
    file.close()

    # --Remove newline characters--
    for line in lines:
        line.replace("\n", "")

    # --Split the lines apart at the delimiters--
    fully_split = []
    
    for line in lines:
        values = []
        last_sep = 0

        # Iterate through each character in the line.
        for char in range(0, len(line)):
        
            # If a delimiter is found or if the end of the line is reached,
            #   append value 'values' and update 'last_sep'.
            if (line[char] == delimiter) or (char == (len(line) - 1)):

                # If it isn't the first value in the list, cut of the
                #   first character as it will be a delimiter. Otherwise, don't.
                if char == 0:
                    values += [line[last_sep:char]]
                else:
                    values += [line[last_sep + 1:char]]
                last_sep = char

        # Append the new set of values for this line to the final list.
        fully_split += [values]

    return fully_split        

# Returns the date in the format dd/mm/yyyy

def short_date():
    # Get the time and date
    d = time.gmtime()

    # Specifically store the day, month and year
    day = str(d.tm_mday)
    mon = str(d.tm_mon)
    yr = str(d.tm_year)

    # If either the month or year are only one digit, add a 0 to
    #   the start.
    if len(day) == 1:
        day = "0" + day

    if len(mon) == 1:
        mon = "0" + mon

    return(day + "/" + mon + "/" + yr)

# Puts a 4 space indent before each of the elements in the
#   list that is passed in

def indent(text):
    # 'text' should be of type string or list and is the text
    #   which will be indented.
    
    # 4 space indent
    INDENT = "    "

    # Handle strings and lists separately
    if type(text) == str:

        # Put an indent after every newline, and one at the start
        indented = INDENT + (text.replace("\n", "\n" + INDENT))

        # Cut off extra indent from end and return
        return(indented[0:-4])
    
    elif type(text) == list:
        
        indented = []

        # For each of the elements, add indents as with a string, and append to 'indented'
        for element in text:
            indented += [(INDENT + (element.replace("\n", "\n" + INDENT))[0:-4])]
        return(indented)
    
    else:
        # If the argument is not of an acceptable type
        raise Exception("This function allows strings and lists only")

def unlistify(text):
    # 'text' should be the list which is to be converted to a
    #   string

    # String will be stored here
    string_text = ""

    # For each of the elements, concatenate it to 'string_text'
    for element in text:
        string_text += element

    return(string_text)

def locate(haystack, needle):
    # Find first occurence of 'needle' in 'haystack'
    for check in range(len(haystack)):
        if haystack[check] == needle:
            return check
        elif check == len(haystack)-1:
            return None

def keyword_convert(properties):
    keywords = {}
    for prop in properties:
        key = prop[:locate(prop, "=")]
        key = key.replace(" ","")

        val = prop[locate(prop, "=")+1:]
        if val[0] == " ":
            val = val[1:]
            
        if ((val[0] == "\"") and (val[-1] == "\"")) or ((val[0] == "'") and (val[-1] == "'")):
            val = val[1:-1]

        if val == "$NULL$":
            val = None
        keywords[key] = val

    return keywords

def image_remove(keyword_props):
    new_dict = {}
    for key in keyword_props.keys():
        if key != "image":
            new_dict[key] = keyword_props[key]
        
    return new_dict

def image_unstring(string):
    return PhotoImage(file=string[20:-2])
    
def prompt_type(prop, additional):
    valid_props = ["width", "height", "text", "image", "cursor",
                   "takefocus", "values", "justify", "length",
                   "maximum", "orient", "mode"]
    
    if prop in valid_props:
        if prop == "width":
            return {"window_type":"Single",
                    "title":"Width",
                    "message":"Please specify a width:",
                    "single_type":"int",
                    "single_preload":additional}
        
        elif prop == "height":
            return {"window_type":"Single",
                    "title":"Height",
                    "message":"Please specify a height:",
                    "single_type":"int",
                    "single_preload":additional}
        
        elif prop == "text":
            return {"window_type":"Single",
                    "title":"Text",
                    "message":"Please specify some text:",
                    "single_type":"string",
                    "single_preload":additional}
        
        elif prop == "image":
            return {"window_type":"Explorer",
                    "title":None,
                    "message":None}
        
        elif prop == "cursor":
            return {"window_type":"Dropdown",
                    "title":"Cursor",
                    "message":"Please select a cursor to be displayed on hovering:",
                    "combo_values":["arrow", "based_arrow_down", "based_arrow_up", "boat", "bogosity",
                                    "bottom_left_corner", "bottom_right_corner", "bottom_side", "bottom_tee",
                                    "box_spiral", "center_ptr", "circle", "clock", "coffee_mug", "cross",
                                    "cross_reverse", "crosshair", "diamond_cross", "dot", "dotbox",
                                    "double_arrow", "draft_large", "draft_small", "draped_box", "exchange",
                                    "fleur", "gobbler", "gumby", "hand1", "hand2", "heart", "icon",
                                    "iron_cross", "left_ptr", "left_side", "left_tee", "leftbutton",
                                    "ll_angle", "lr_angle", "man", "middlebutton", "mouse", "pencil",
                                    "pirate", "plus", "question_arrow", "right_ptr", "right_side",
                                    "right_tee", "rightbutton", "rtl_logo", "sailboat", "sb_down_arrow",
                                    "sb_h_double_arrow", "sb_left_arrow", "sb_right_arrow", "sb_up_arrow",
                                    "sb_v_double_arrow", "shuttle", "sizing", "spider", "spraycan", "star",
                                    "target", "tcross", "top_left_arrow", "top_left_corner", "top_right_corner",
                                    "top_side", "top_tee", "trek", "ul_angle", "umbrella", "ur_angle", "watch",
                                    "xterm", "X_cursor"],
                    "combo_preload":additional} 
        
        elif prop == "takefocus":
            return {"window_type":"Checkbox",
                    "title":"Take Focus",
                    "message":"Is the widget selectable by tab?",
                    "checkbox_preload":additional}
        
        elif prop == "values":
            return {"window_type":"List",
                    "title":"Values",
                    "message":"Values displayed in the combobox:",
                    "list_preload":additional}
        
        elif prop == "justify":
            return {"window_type":"Dropdown",
                    "title":"Justification",
                    "message":"The justification of the text:",
                    "combo_values":["left", "right", "center"],
                    "combo_preload":additional}
        
        elif prop == "length":
            return {"window_type":"Single",
                    "title":"Length",
                    "message":"The length of the widget:",
                    "single_type":"int",
                    "single_preload":additional}
        
        elif prop == "maximum":
            return {"window_type":"Single",
                    "title":"Maximum Value",
                    "message":"The maximum value the widget can have:",
                    "single_type":"int",
                    "single_preload":additional}
        
        elif prop == "orient":
            return {"window_type":"Dropdown",
                    "title":"Orientation",
                    "message":"The orientation of the the widget:",
                    "combo_values":["horizontal","vertical"],
                    "combo_preload":additional}
        
        elif prop == "mode":
            return {"window_type":"Dropdown",
                    "title":"Progress Bar Mode",
                    "message":"Whether the progress bar is determinate or indeterminate:",
                    "combo_values":["determinate","indeterminate"],
                    "combo_preload":additional}

def property_strip(prop):
    
    for char in range(len(prop)):
        if prop[char] == "=":
            return prop[:char]
            

def property_find(properties, find):
    # Remove spaces from everything
    find = find.replace(" ","")
    
    nospace = []
    for prop in properties:
        nospace += [prop.replace(" ","")]

    # Strip data away from all args
    find = property_strip(find)

    stripped = []
    for prop in nospace:
        stripped += [property_strip(prop)]
        
    # Get the index
    return locate(stripped, find)
    
def coord_validate(x, y, window_width, window_height, buffer = 5, negative_check = False, widg_height = None, widg_width = None):
    # This function determines whether a widget will be moved off the window and proposes a new location.
    # Allow minimum of 5 by 5px of the widget to be onscreen.
    
    if (type(x) == str) and (type(y) == str): 
        x = x.replace(" ", "")
        y = y.replace(" ", "")
        
        if x[1] == "=":
            x = x[2:]
        
        if y[1] == "=":
            y = y[2:]
            
        x = int(x)
        y = int(y)
        
    window_width = int(window_width)
    window_height = int(window_height)
    
    new = [x, y]
    
    err = False
    if x > window_width - buffer:
        err = True
        new[0] = window_width - 10
        
    if y > window_height - buffer:
        err = True
        new[1] = window_height - 10
    
    if negative_check:
        if x + widg_width <= 1:
            err = True
            new[0] = 10 - widg_width
        
        if y + widg_height <= 1:
            err = True
            new[1] = 10 - widg_height
            
    return [err, new]
    
def remove_unused(widgets):
    widgets_out = []
    
    for widget in range(len(widgets)):
        widget_out = []
        for prop in range(len(widgets[widget])):
            if "$NULL$" in widgets[widget][prop]:
                widget_out += [None]
                
            elif type(widgets[widget][prop]) == list:
                cleaned = []
                
                for sub in range(len(widgets[widget][prop])):
                    #print(widgets[widget][prop][sub])
                    if "$NULL$" not in widgets[widget][prop][sub]:
                        cleaned += [widgets[widget][prop][sub]]
                        
                widget_out += [cleaned]
                
            else:
                widget_out += [widgets[widget][prop]]            
                
        widgets_out += [widget_out]
                    
    return widgets_out

def method_assemble(identifier, method, arguments):
    if type(arguments) == str:
        return identifier + "." + method + "('" + str(arguments) + "')"
    elif type(arguments) == list:
        result = identifier + "." + method + "("
        for ii in arguments:
            result += str(ii)
            result += ","
        result = result[:-1]
            
        return result + ")"

def string_list_parse(string_list):
    string_list = string_list[1:]
    result = []
    
    in_string = False
    current_string_terminator = None
    term = ""
    
    for char in string_list:

        if ((char == '"') or (char == "'")) and not in_string:
            current_string_terminator = char
            in_string = True

        elif in_string and (char == current_string_terminator):
            in_string = False
            current_string_terminator = None
        
        if in_string and (char != current_string_terminator):
            term += char
            
        if ((char == ",") or (char == "]")) and not in_string:
            result += [term]
            term_is_string = False
            term = ""
                        
    return result
        
def type_fix(keyword_dict):
    list_types = ["values"]
    bool_tuple_types = ["resizable"]
    
    for key in keyword_dict.keys():
        if key in list_types:
            if keyword_dict[key] != None:
                keyword_dict[key] = string_list_parse(keyword_dict[key])
        if key in bool_tuple_types:
            keyword_dict[key] = keyword_dict[key][1:-1].split(",")
            
    return keyword_dict

def bool_list_parse(string):
    if type(string) == str:
        listified = string[1:-1].split(", ")
        
        for element in range(len(listified)):
            if listified[element] == "True":
                listified[element] = True
            else:
                listified[element] = False
            
        return listified
    else:
        return string

def quote_escape(prop):
    string_properties = ["text"]
    
    value = prop[locate(prop, "=") + 1:]
    if value[0] == " ":
        value = value[1:]
        
    escaped = ""
    if property_strip(prop.replace(" ","")) in string_properties:
        for char in range(len(value)):
            current = value[char]
            if ((char != 0) and (char != len(value) - 1)) and (current == "\""):
                current = "\\\""
            escaped += current
            
        return property_strip(prop.replace(" ", "")) + " = " + escaped
    else:
        return prop

def dict_pair_delete(dictionary, del_key):
    new_dict = {}
    for key in dictionary.keys():
        if key != del_key:
            new_dict[key] = dictionary[key]
    return new_dict
        
#print(quote_escape("text = \"thisiss\"ometext\""))

#print(noneify([1,2,3,4], [['ttk.Button', '$NULL$', 'root', 'x=127', 'y=52', ['width = $NULL$', 'text = "Button"'], [], []], ['ttk.Button', 'widget_1', 'root', 'x=67', 'y=117', ['width = $NULL$', 'text = "Button"'], [], []]]))
#print(remove_unused([['ttk.Button', '$NULL$', 'root', 'x=127', 'y=52', ['width = $NULL$', 'text = "Button"'], [], []], ['ttk.Button', 'widget_1', 'root', 'x=67', 'y=117', ['width = $NULL$', 'text = "Button"'], [], []]]))