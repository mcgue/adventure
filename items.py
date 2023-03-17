# Base for all items
class Item():
    """Base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"{self.name}\n=====\n{self.description}\nValue: {self.value}\n"

# Items of value
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