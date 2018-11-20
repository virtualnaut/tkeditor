# GENERAL TOOLS
# 12/11/18
# This module contains functions that are useful throughout the whole
#    project.

import time

# This will be used to read the CSV file which contains the properties
#   and names of the widgets.

def csv_parse(path, separator = ","):
    # 'path' is the location of the txt/csv file in the file system.
    # 'separator' is the character that has been used in the file
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

    # --Split the lines apart at the commas (or at the separators)--
    fully_split = []
    
    for line in lines:
        values = []
        last_sep = 0

        # Iterate through each character in the line.
        for char in range(0, len(line)):
        
            # If a separator is found or if the end of the line is reached,
            #   append value 'values' and update 'last_sep'.
            if (line[char] == separator) or (char == (len(line) - 1)):

                # If it isn't the first value in the list, cut of the
                #   first character as it will be a separator. Otherwise, don't.
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
