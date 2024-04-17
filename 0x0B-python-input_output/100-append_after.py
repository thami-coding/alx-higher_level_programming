"""
Module: file_modifier

This module contains a function for inserting a line of text into a file after each line containing a specific string.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line containing a specific string.

    Parameters:
    - filename (str): The name of the file to modify.
    - search_string (str): The string to search for in each line.
    - new_string (str): The line of text to insert after each line containing the search string.
    """
    # Open the file for reading and writing
    with open(filename, 'r+') as file:
        # Read all lines from the file
        lines = file.readlines()
        
        # Rewind the file pointer to the beginning
        file.seek(0)
        
        # Iterate through the lines
        for line in lines:
            # Write the current line
            file.write(line)
            # If the current line contains the search string, write the new string after it
            if search_string in line:
                file.write(new_string + '\n')
        
        # Truncate the file to remove any remaining content beyond the current position
        file.truncate()
