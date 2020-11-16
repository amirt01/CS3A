"""
Assignment One: Gork
Author: Amir Tadros
CWID: 20402155
Date: 10/18/2020

Enhancements in this release:
- Added a welcome function to ask the player how many people are on the ship
- Added a menu to run the Gork game
- Added a main function to start or exit the game.
"""

import Lab3

"""
Purpose: Display the background story that includes the following information.
         Ask the user how many personnel are on the ship and return the
         response.
Parameters: None
Return: The number of personnel on the ship.
"""


def welcome() -> int:
    print(
        "You are in charge of a top secret military mission when your space"
        "\nship makes an emergency landing on the largest moon of planet"
        "\nGork. The space ship is damaged. Oxygen levels in the space ship"
        "\nbegin to drop. ")
    print("How many military personnel are on your ship?")
    personnel: int = int(input("Number of personnel: "))
    if personnel <= 0:
        print("You must enter a positive number...")
        exit()
    return personnel


"""
Purpose: Allow the user to make a choice about what to do. Reply with the
         correct output and proper calculations.
Parameters: The number of personnel as an integer.
Return: None
"""


def menu(personnel: int) -> None:
    print("Choose one:")
    print("1. Attempt repairs on the ship")
    print("2. Request an emergency rescue from mission command")
    print("3. Break protocol and reveal the top secret space ship's location")
    choice: int = int(input("Your choice: "))
    if choice == 1:
        print("Toxic material on the moon has corroded the launch gear and the"
              "launch exploded.")
    elif choice == 2:
        print("The oxygen was depleted before the rescue team arrived. There"
              "\nwere 4 people killed.")
        if personnel > 3:
            print("The percentage of people rescued is " +
                  str(Lab3.calculatePct(personnel, 4)))
        else:
            print("The percentage of people rescued is 0")
    elif choice == 3:
        print("The Russians agree to send a rescue ship, but secretly attempt"
              "\nto hack into the ships systems remotely, which triggers an"
              "\nautomatic shut down of all communications systems and locks"
              "\nall mission critical storage units, including one of the"
              "\nstorage unit that holds emergency oxygen tanks. One quarter"
              "\n(.25) of all personnel are lost.")
        print("The number of surviving personnel is " +
              str(Lab3.calculateTotal(personnel, .25)))
    else:
        print("You have been eaten by a Grue.")


def main() -> None:
    print("Welcome to Gork 1.0!")
    print("Created by Amir Tadros")
    playing: bool = True
    while playing:
        print("What would you like to do?")
        print("1. Play Gork")
        print("2. Exit")
        if int(input("Your choice: ")) == 1:
            menu(welcome())
        else:
            playing = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

"""
Welcome to Gork 1.0!
Created by Amir Tadros
What would you like to do?
1. Play Gork
2. Exit
Your choice: 1
You are in charge of a top secret military mission when your space
ship makes an emergency landing on the largest moon of planet
Gork. The space ship is damaged. Oxygen levels in the space ship
begin to drop. 
How many military personnel are on your ship?
Number of personnel: 8
Choose one:
1. Attempt repairs on the ship
2. Request an emergency rescue from mission command
3. Break protocol and reveal the top secret space ship's location
Your choice: 1
Toxic material on the moon has corroded the launch gear and thelaunch exploded.
"""

"""
Welcome to Gork 1.0!
Created by Amir Tadros
What would you like to do?
1. Play Gork
2. Exit
Your choice: 1
You are in charge of a top secret military mission when your space
ship makes an emergency landing on the largest moon of planet
Gork. The space ship is damaged. Oxygen levels in the space ship
begin to drop. 
How many military personnel are on your ship?
Number of personnel: 8
Choose one:
1. Attempt repairs on the ship
2. Request an emergency rescue from mission command
3. Break protocol and reveal the top secret space ship's location
Your choice: 2
The oxygen was depleted before the rescue team arrived. There
were 4 people killed.
The percentage of people rescued is 0.5
"""

"""
Welcome to Gork 1.0!
Created by Amir Tadros
What would you like to do?
1. Play Gork
2. Exit
Your choice: 1
You are in charge of a top secret military mission when your space
ship makes an emergency landing on the largest moon of planet
Gork. The space ship is damaged. Oxygen levels in the space ship
begin to drop. 
How many military personnel are on your ship?
Number of personnel: 8
Choose one:
1. Attempt repairs on the ship
2. Request an emergency rescue from mission command
3. Break protocol and reveal the top secret space ship's location
Your choice: 3
The Russians agree to send a rescue ship, but secretly attempt
to hack into the ships systems remotely, which triggers an
automatic shut down of all communications systems and locks
all mission critical storage units, including one of the
storage unit that holds emergency oxygen tanks. One quarter
(.25) of all personnel are lost.
The number of surviving personnel is 6
"""