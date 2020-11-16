"""
Assignment Two: Disaster Calculator
Author: Amir Tadros
CWID: 20402155
Date: 10/2/2020

Enhancements in this release:
- Use two functions to calculate the percentage of people who survived a
  disaster and the number of people who survived a disaster.
"""

"""
Purpose: Calculate the percentage of people who survived a disaster.
Parameters: The number of people in the disaster zone and the number of people
             killed.
Return: The percentage of people who survived a disaster.
"""


def calculatePct(ppl_in_zone, ppl_killed) -> float:
    return round((ppl_in_zone - ppl_killed) / ppl_in_zone, 2)


"""
Purpose: Calculate the total number of people who survived a disaster.
Parameters: The number of people in the disaster zone and the percentage of
            people killed.
Return: The total number of people who survived.
"""


def calculateTotal(ppl_in_zone, pct_killed) -> int:
    return round(ppl_in_zone - ppl_in_zone * pct_killed)


def main(name) -> None:
    print("CalculatePct function test:")
    print("100 people in the disaster zone and 25 people killed: " +
          str(calculatePct(100, 25)))

    print("214 people in the disaster zone and 41 people killed: " +
          str(calculatePct(214, 41)))

    print("854 people in the disaster zone and 2 people killed: " +
          str(calculatePct(854, 2)))

    print("\nCalculateTotal function test:")
    print("100 people in the disaster zone and 25% of people killed: " +
          str(calculateTotal(100, .25)))

    print("937 people in the disaster zone and 3% of people killed: " +
          str(calculateTotal(937, .3)))

    print("143 people in the disaster zone and 16% of people killed: " +
          str(calculateTotal(143, .16)))


if __name__ == '__main__':
    main('PyCharm')

"""
CalculatePct function test:
100 people in the disaster zone and 25 people killed: 0.75
214 people in the disaster zone and 41 people killed: 0.81
854 people in the disaster zone and 2 people killed: 1.0

CalculateTotal function test:
100 people in the disaster zone and 25% of people killed: 75
937 people in the disaster zone and 3% of people killed: 656
143 people in the disaster zone and 16% of people killed: 120
"""