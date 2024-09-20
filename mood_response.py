'''
1. Python Modules and Data Handling Assignment
Objective: The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, 
and to apply data handling techniques using Python's data structures and error handling.

Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module that asks the user 
how they are feeling today and responds with a custom message based on the mood entered. -
'''

def mood_response(mood):
    if mood == 'happy':
        print("I'm glad to hear that you are happy!")
    elif mood == 'sad':
        print("Sorry to hear that, hope you feel better.")
    elif mood == 'mad':
        print("Cheer up, no need to be angry.")
    else:
        print("Goodbye!")
