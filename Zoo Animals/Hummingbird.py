"""
Project Zoo Animal
Author: Jennifer Helguera
Date: 11/19/2020

Enhancements in this release:
Design, implement, and use classes and objects

"""


class hummingbird:

    # Constructor
    def __init__(self):
        self.animalType = "Hummingbird"
        self.idTag = None
        self.minTemperature = 35
        self.maxTemperature = 100

    # Instance Methods

    # mutator ("set") methods -------------------------------

    def setIdTag(self, anIdTag):
        self.idTag = anIdTag

    # accessor ("get") methods -------------------------------

    def getAnimalType(self):
        return self.animalType

    def getIdTag(self):
        return self.idTag

    def getMinTemperature(self):
        return self.minTemperature

    def getMaxTemperature(self):
        return self.maxTemperature

"""
s = hummingbird()
print("Animal:", s.getAnimalType(), "\nMin Temperature:",
      s.getMinTemperature(),
      "\nMax Temperature:", s.getMaxTemperature(), "\nID Tag:",
      s.getIdTag())
"""
