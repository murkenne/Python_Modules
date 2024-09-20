'''
2. Mastering Python Modules and Aliases
Objective: The aim of this assignment is to enhance your proficiency in using Python modules, 
both standard and custom, with a specific focus on importing with aliases.

Task 1: Custom Module with Aliases 

Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation 
(e.g., reversing a string, capitalizing). In your main script, 
import this module using an alias and utilize its functions.
'''

# main1.py

# test_text_utils.py

import text_utils as tu

# Test the reverse_string function
print(tu.reverse_string("hello"))

# Test the capitalize_string function
print(tu.capitalize_string("hello"))
