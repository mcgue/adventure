# Text-Based Adventure Game With Classes
# Based on:
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/
# In progress

import time

# Base for all items
class Item():
    """Base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description,self.value)

# Tell objective
# print("The object is to find the key and unlock the jeweled box."
#      "The key is in one of the rooms")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Introduction
    print("Let\'s play Adventure")
    # Obtain player's name
    player_name = input("What do you want to call your character?")
    print_hi(player_name)