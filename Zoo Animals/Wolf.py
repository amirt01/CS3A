"""
Assignment: Mandatory Discussion - Zoo Animals
Author: Wai TANG
Date: 11/19/2020

My first name begins with W, so I create a Wolf class
that includes the instance methods listed in guidelines.
"""


class Wolf:

    def __init__(self):
        self.animalType = "Wolf"
        self.idTag = None
        self.minTemperature = -70.0
        self.maxTemperature = 120.0

    def setIdTag(self, anIdTag):
        self.idTag = anIdTag

    def getIdTag(self):
        return self.idTag

    def getAnimalType(self):
        return self.animalType

    def getMinTemperature(self):
        return self.minTemperature

    def getMaxTemperature(self):
        return self.maxTemperature

"""
# instantiate two Wolf objects in main
northwestern_wolf = Wolf()
mexican_wolf = Wolf()

# initialize northwestern_wolf
northwestern_wolf.idTag = "001"
northwestern_wolf.minTemperature = -70.0
northwestern_wolf.maxTemperature = 30.0

# initialize mexican_wolf
mexican_wolf.idTag = "002"
mexican_wolf.minTemperature = 60.0
mexican_wolf.maxTemperature = 120.0

print("Animal type of Northwestern Wolf is", northwestern_wolf.animalType)
print("Id tag is", northwestern_wolf.idTag)
print("Min temperature is", northwestern_wolf.minTemperature)
print("Max temperature is", northwestern_wolf.maxTemperature)

print("\nAnimal type of Mexican Wolf is", mexican_wolf.animalType)
print("Id tag is", mexican_wolf.idTag)
print("Min temperature is", mexican_wolf.minTemperature)
print("Max temperature is", mexican_wolf.maxTemperature)
"""

""" --------------------------- RUN -------------------------------

Animal type of Northwestern Wolf is Wolf
Id tag is 001
Min temperature is -70.0
Max temperature is 30.0

Animal type of Mexican Wolf is Wolf
Id tag is 002
Min temperature is 60.0
Max temperature is 120.0
>>>

--------------------------- END RUN ------------------------------- """
