# Text-Based Adventure Game With Classes
# Based on:
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-2-the-world-space/
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
        return f"{self.name}\n=====\n{self.description}\nValue: {self.value}\n"

class Jewel(Item):
    def __init__(self, color):
        self.color = color
        super().__init__(name="Gold",
                         description="A {} jewel.".format(str(self.color)),
                         value=self.color)

# Helps in game, used is times can help, help is how much can help
class Partner:
    def __init__(self, name, used, help):
        self.name = name
        self.used = used
        self.help = help

    def is_alive(self):
        return self.used > 0

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