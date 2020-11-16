"""
Assignment Five: DMV Grader
Author: Amir Tadros
CWID: 20402155
Date: 11/7/2020

Enhancements in this release:
- Add correct answer list
- Add required input (A-D)
- Add accumulator variable
- Display score and percentage
- Add test run
- Add docstr
- Add sample run
"""


def main():
    # correct answer list
    correct_answers: list = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D',
                             'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
    # valid answer list
    valid_answers: list = ['A', 'B', 'C', 'D']

    # the current question being answered
    question: int = 1
    # the current number of correct answers
    score: int = 0
    for correct_answer in correct_answers:
        # while the user hasn't answered a valid answer
        while True:
            # get the answer from the user and capitalize it
            user_answer: str = input(
                "Answer for question " + str(question) + ": ").capitalize()
            # check if the answer is in the list of valid options
            if user_answer in valid_answers:
                # if the answer is correct, add one to the score
                # else, add zero
                score += user_answer == correct_answer
                # break the loop because the answer was valid
                break
            # if the answer isn't valid
            else:
                # tell the user to enter a valid answer
                print("Please input a valid correct (A - D)")
        # move on to the next question
        question += 1
    # print the score
    print("Score: " + str(score))
    # print the percentage
    print("Percentage: " + str(score / len(correct_answers)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

"""
Answer for question 1: b
Answer for question 2: D
Answer for question 3: z
Please input a valid correct (A - D)
Answer for question 3: A
Answer for question 4: a
Answer for question 5: c
Answer for question 6: a
Answer for question 7: b
Answer for question 8: a
Answer for question 9: c
Answer for question 10: d
Answer for question 11: b
Answer for question 12: c
Answer for question 13: d
Answer for question 14: a
Answer for question 15: d
Answer for question 16: c
Answer for question 17: c
Answer for question 18: b
Answer for question 19: d
Answer for question 20: a
Score: 20
Percentage: 1.0
"""
