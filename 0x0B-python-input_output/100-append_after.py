#!/usr/bin/python3
"""
This function reads the contents of the input file line by line
uisng the readline() function

rememebr the readline() returns a list of of the lines in teh file

so here the list of the lines is stored in the variable lines.

we open the file again in write mode this time and iterate over the
st that we have now of line that is lines

and for each line it reads, it writes the line to the output file.

while writing we check if the line contains the specified search str

if it does we write a new string after it.
remember we are using 'w' so it overwites what was there before
starts aftresh while looking fo the search string.

we have what we are writing already in the list we have already
returned in the lines with the help of the readline() method
"""


def append_after(filename="", search_string="", new_string=""):
    """
    this function does the opening of the file in read mode
    it also does the write mode to write it newly while including the
    the new string afte the search string
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        list_lines = f.readlines()

    with open(filename, mode='w', encoding="utf-8") as f:
        for line in list_lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
