"""
Assignment: Mandatory Discussion, Zoo Animals
Author: Nicolette Bahr
Date: 11/20/2020

Objective: Design, implement, and use classes and objects

"""


class Narwhal:
    def __init__(self):
        self.animalType = "Narwhal"
        self.idTag = 1001
        self.minTemperature = 29
        self.maxTemperature = 37.4

    def setIdTag(self, anIdTag):
        self.idTag = anIdTag
        return self.idTag

    def getAnimalType(self):
        return self.animalType

    def getIdTag(self):
        return self.idTag

    def getMinTemperature(self):
        return self.minTemperature

    def getMaxTemperature(self):
        return self.maxTemperature

"""
# There are not different types of Narwhals but this is just to demonstrate the program
Southern_Narwhal = Narwhal()
print("Animal Type: ", Southern_Narwhal.animalType)
print("ID Tag: ", Southern_Narwhal.idTag)
print("Natural Habit Temperature Range: ", Southern_Narwhal.minTemperature, "-",
      Southern_Narwhal.maxTemperature)
"""

"""
Animal Type: Narwhal
ID Tag: 1001
Natural Habit Temperature Range: 29 - 37.4
"""
