"""
Assignment Two: Disaster Calculator
Author: Amir Tadros
CWID: 20402155
Date: 10/2/2020

Enhancements in this release:
- remove main function
"""

import math

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
    return math.floor(ppl_in_zone - ppl_in_zone * pct_killed)
