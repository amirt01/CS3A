"""
Assignment Two: Shape Shifter
Author: Amir Tadros
CWID: 20402155
Date: 10/1/2020

Enhancements in this release:
- Use a function to print each basic shape instead of
  storing the strings in a variable.
"""


def line() -> None:
    print("       *")
    print("       *")


def triangle() -> None:
    print("       *")
    print("      * *")
    print("     *   *")
    print("    *     *")
    print("   *       *")
    print("  ***********")


def rectangle() -> None:
    print("  ***********")
    print("  *         *")
    print("  *         *")
    print("  *         *")
    print("  ***********")


def main() -> None:
    print("Line")
    line()

    print("Triangle")
    triangle()

    print("Rectangle")
    rectangle()

    print("Beeker")
    line()
    triangle()

    print("Tree")
    triangle()
    line()

    print("House")
    triangle()
    rectangle()


if __name__ == "__main__":
    main()

"""
Line
       *
       *
Triangle
       *
      * *
     *   *
    *     *
   *       *
  ***********
Rectangle
  ***********
  *         *
  *         *
  *         *
  ***********
Beeker
       *
       *
       *
      * *
     *   *
    *     *
   *       *
  ***********
Tree
       *
      * *
     *   *
    *     *
   *       *
  ***********
       *
       *
House
       *
      * *
     *   *
    *     *
   *       *
  ***********
  ***********
  *         *
  *         *
  *         *
  ***********
"""
