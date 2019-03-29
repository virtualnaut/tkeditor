# GENERAL TOOLS
# 12/11/18
# This module contains functions that are useful throughout the whole
#    project.

import time

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
        print(key)

        val = prop[locate(prop, "=")+1:]
        if val[0] == " ":
            val = val[1:]
            
        if ((val[0] == "\"") and (val[-1] == "\"")) or ((val[0] == "'") and (val[-1] == "'")):
            val = val[1:-1]
            
        keywords[key] = val

    return keywords

#print(keyword_convert(["text = 'Click'", "width = 20"]))





        
