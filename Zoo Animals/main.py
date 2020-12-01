"""
Assignment Five: Zoo Animals
Author: Amir Tadros
CWID: 20402155
Date: 11/23/2020

Enhancements in this release:
- error checking for proper input
- search function for finding an animal id in a list
- stats function for printing every accessor
- demo function for printing animal stats in a list
- list of animals in main function
- user input and well formatted output
"""

from Bison import Bison
from Hummingbird import hummingbird as Hummingbird
from Narwhal import Narwhal
from Tapir import Tapir
from Wolf import Wolf


def search(animals: list, animalId: int):
    for animal in animals:
        if animal.getIdTag() == animalId:
            return animal
    return -1


# print each accessory from an animal
def stats(animal):
    print("Animal Type: " + str(animal.getAnimalType()))
    print(str(animal.getAnimalType()) + " Min Temp: " + str(
        animal.getMinTemperature()))
    print(str(animal.getAnimalType()) + " Max Temp: " + str(
        animal.getMaxTemperature()))


# loop through every animal and print their statistics
def demo(animals: list):
    for animal in animals:
        print()
        stats(animal)
        print()


def main():
    # Initialize each animal in a list
    animals: list = [Tapir(), Bison(), Hummingbird(), Narwhal(), Wolf()]

    for animal in animals:
        while True:
            try:
                animalId = int(input(
                    "Please input your " + str(
                        animal.getAnimalType()) + "'s Id Tag: "))

                # Test if the inputted id number already exists
                if search(animals, animalId) != -1:
                    print("Oops! That id number already exists. Try again...")
                    continue

                # Assign the inputted id number to the current animal
                animal.setIdTag(animalId)
                break
            except ValueError:
                print("Oops! That was not a valid number. Try again...")

    while True:
        while True:
            try:
                animalId = int(
                    input("Please input the animal id number, or 0 for the "
                          "demo: "))
                break
            except ValueError:
                print("Oops! That was not a valid number. Try again...")
        print()

        if animalId == 0:
            demo(animals)
            break

        animal = search(animals, animalId)

        if animal == -1:
            print("Oops! That id number does not match any animal in our "
                  "database. Try again...")
            continue

        stats(animal)
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

"""
Please input your Tapir's Id Tag: 1
Please input your Bison's Id Tag: a
Oops! That was not a valid number. Try again...
Please input your Bison's Id Tag: 2
Please input your Hummingbird's Id Tag: 3
Please input your Narwhal's Id Tag: 2
Oops! That id number already exists. Try again...
Please input your Narwhal's Id Tag: 4
Please input your Wolf's Id Tag: 5
Please input the animal id number, or 0 for the demo: 2

Animal Type: Bison
Bison Min Temp: -40.0
Bison Max Temp: 110.0

Please input the animal id number, or 0 for the demo: 6

Oops! That id number does not match any animal in our database. Try again...
Please input the animal id number, or 0 for the demo: 4

Animal Type: Narwhal
Narwhal Min Temp: 29
Narwhal Max Temp: 37.4

Please input the animal id number, or 0 for the demo: 0


Animal Type: Tapir
Tapir Min Temp: 65
Tapir Max Temp: 85


Animal Type: Bison
Bison Min Temp: -40.0
Bison Max Temp: 110.0


Animal Type: Hummingbird
Hummingbird Min Temp: 35
Hummingbird Max Temp: 100


Animal Type: Narwhal
Narwhal Min Temp: 29
Narwhal Max Temp: 37.4


Animal Type: Wolf
Wolf Min Temp: -70.0
Wolf Max Temp: 120.0


Process finished with exit code 0
"""
