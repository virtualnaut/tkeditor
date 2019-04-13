def clean(data):
    # This function replaces nulls with nothing, as nulls will be used in the file for delimiting.
    return str(data).replace("\0","")
    
def save_data(path, root, widgets):
    delimiter = "\0"
    lines = []
    
    lines += ["!##ROOTDATA"]
    for element in range(4):
        lines += [clean(root[element])]
        
    lines += ["!PROPERTIES"]
    for prop in root[4]:
        lines += [clean(prop)]
        
    lines += [delimiter]    
    
    lines += ["!#METHODS"]
    for key in root[5][0].keys():
        lines += [clean(key)]
        lines += [clean(root[5][0][key])]
        
    lines += [delimiter]
        
    lines += ["!#BINDINGS"]
    # Feature not implemented
    
    lines += [delimiter]
    
    for widget in widgets:
        lines += ["!##WIDGETDATA"]
        for element in range(5):
            lines += [clean(widget[element])]
            
        lines += ["!PROPERTIES"]
        for prop in widget[5]:
            lines += [clean(prop)]
            
        lines += [delimiter]    
        
        lines += ["!#METHODS"]
        for key in widget[6][0].keys():
            lines += [clean(key)]
            lines += [clean(root[6][0][key])]
            
        lines += [delimiter]
            
        lines += ["!#BINDINGS"]
        # Feature not implemented            
            
        lines += [delimiter + delimiter]
    
    delimited = []
    for line in lines:
        delimited += line + delimiter
        
    concatted = ""
    for line in delimited:
        concatted += line
        
    # Remove extra nulls
    concatted = concatted[:-4]
        
    file = open(path, "w+")
    file.write(concatted)
    file.close()


def load_data(path):
    delimiter = "\n"

    file = open(path, "r")
    file_data = file.read()
    file.close()

    chop_down = file_data.split("\0\0\0\0")
    for layer_1 in range(len(chop_down)):
        chop_down[layer_1] = chop_down[layer_1].split("\0\0\0")
        for layer_2 in range(len(chop_down[layer_1])):
            chop_down[layer_1][layer_2] = chop_down[layer_1][layer_2].split("\0\0")
            for layer_3 in range(len(chop_down[layer_1][layer_2])):
                chop_down[layer_1][layer_2][layer_3] = chop_down[layer_1][layer_2][layer_3].split("\0")
   
    c = chop_down
            
    root = [c[0][0][0][1], c[0][0][0][2], c[0][0][0][3], c[0][0][0][4], c[0][0][0][6:], [{}], c[0][2][0][1:]]
    
    # Get root methods
    for ii in range(len(c[0][1][0][1:])):
        if ii % 2 == 1:
            root[5][0][c[0][1][0][ii]] = c[0][1][0][ii + 1]

    del c[0][:3]
    
    location = {}
    widgets = []
    
    for widget in range(len(c)):
        widget_data = [c[widget][0][0][1], c[widget][0][0][2], c[widget][0][0][3], c[widget][0][0][4], c[widget][0][0][5], c[widget][0][0][7:], [{}], []]
        location[c[widget][0][0][2]] = widget
        for ii in range(len(c[0][1][0][1:])):
            if ii % 2 == 1:
                widget_data[5][0][c[widget][1][0][ii]] = c[widget][1][0][ii + 1]      
                
        widgets += [widget_data]

    return [root, widgets, location]