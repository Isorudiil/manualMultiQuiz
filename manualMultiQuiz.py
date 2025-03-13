# prompt user with 10 multiplication questions
# ranging from 0 x 0 to 9 x 9

# TODO: User gets three tries to enter the correct answer before program moves on to next question

# TODO: Question marked incorrect after 8 seconds

import random as r
import time as t

QUESTIONQTY = 10
TRIES = 3
MAXTIME = 8

correctAnswers = 0


for question in range(1, QUESTIONQTY + 1):
    num1 = r.randint(0, 9)
    num2 = r.randint(0, 9)
    quotient = num1 * num2
    wrongAnswers = 0
    startTime = t.time()
    while wrongAnswers < TRIES:
        answer = int(input(f'#{question}: {num1} x {num2} = '))
        # user input incorrect answer, so 'Incorrect!' displays
        if answer != quotient:
            print('Incorrect!\n')
            wrongAnswers += 1
            continue
        # user input correct answer, so 'Correct!' displays
        if answer == quotient:
            if startTime + MAXTIME < t.time():
                break
            else:
                print('Correct!\n')
                t.sleep(1)
                correctAnswers += 1
                break

print('\nYou got %i correct answers!\n' % (correctAnswers))