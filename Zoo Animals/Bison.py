"""
Assignment: Zoo Animals
Author: Eric Belden
Date: 11/18/2020

Enhancements in this release:
- Create a zoo animal "class" for Bison
"""


class Bison:

    # initializer ("constructor") method ---------------------
    # Bisons (not the same as Buffaloes) are represented by
    # two groups, the American Bison and the European Bison.
    # Bison can survive the scorching heat of Texas and
    # the extreme cold of Yellowstone Park.
    # FYI: Buffaloes are found in Africa and South Asia.

    def __init__(self):
        self.animalType = "Bison"
        self.idTag = None
        self.minTemperature = -40.0
        self.maxTemperature = 110.0

    # mutator ("set") methods -------------------------------

    # Sets an Id tag, but not sure if ultimately the Id can be null,
    # or if the Id should be unique for a specific zoo.
    # Also, not sure who would be granted access to this mutator.

    def setIdTag(self, anIdTag):
        self.idTag = anIdTag
        return True

    # accessor ("get") methods -------------------------------

    def getAnimalType(self):
        return self.animalType

    def getIdTag(self):
        return self.idTag

    def getMinTemperature(self):
        return self.minTemperature

    def getMaxTemperature(self):
        return self.maxTemperature

# Example: define Bison object and print some details ------
# american_bison = Bison()
# print(american_bison.animalType)
# print(american_bison.minTemperature)
# print(american_bison.maxTemperature)
