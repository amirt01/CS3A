"""
Assignment Two: Shape Shifter
Author: Amir Tadros
CWID: 20402155
Date: 9/23/2020
"""


def main() -> None:
    strLine = "       *\n" \
              "       *"

    strTriangle = "       *\n" \
                  "      * *\n" \
                  "     *   *\n" \
                  "    *     *\n" \
                  "   *       *\n" \
                  "  ***********"

    strRectangle = "  ***********\n" \
                   "  *         *\n" \
                   "  *         *\n" \
                   "  *         *\n" \
                   "  ***********"

    print("Line")
    print(strLine)

    print("Triangle")
    print(strTriangle)

    print("Rectangle")
    print(strRectangle)

    print("Beeker")
    print(strLine)
    print(strTriangle)

    print("Tree")
    print(strTriangle)
    print(strLine)

    print("House")
    print(strTriangle)
    print(strRectangle)


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
