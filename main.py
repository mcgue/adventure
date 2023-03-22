# Text-Based Adventure Game With Classes
# In progress but not currently working on
# Based on:
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-2-the-world-space/
# In progress

import time

# Tell objective
# print("The object is to ?? ")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Introduction
    print("Let\'s play Adventure")
    # Obtain player's name
    player_name = input("What do you want to call your character? ")
    print_hi(player_name)