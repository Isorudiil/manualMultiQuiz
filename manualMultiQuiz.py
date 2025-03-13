# prompt user with 10 multiplication questions
# ranging from 0 x 0 to 9 x 9

# TODO: User enters correct answer, display 'Correct!'

# TODO: User gets three tries to enter the correct answer before program moves on to next question

# TODO: Question marked incorrect after 8 seconds

import random as r
import time as t

QUESTIONQTY = 10
TRIES = 3
correctAnswers = 0

# for question in range(1, QUESTIONQTY + 1):
#     num1 = r.randint(0, 9)
#     num2 = r.randint(0, 9)
#     quotient = num1 * num2
#     for wrong_answer in range(TRIES):
#         time = t.time()
#         timeout = t.time() + 8
#         while time < timeout:
#             answer = int(input(f'#{question}: {num1} x {num2} = '))
#             if answer != quotient:
#                 print('Incorrect!\n')
#                 break

for question in range(1, QUESTIONQTY + 1):
    num1 = r.randint(0, 9)
    num2 = r.randint(0, 9)
    quotient = num1 * num2    
    time = t.time()
    timeout = t.time() + 8
    wrongAnswers = 0
    while time < timeout or wrongAnswers <= TRIES:
        time = t.time()
        timeout = t.time() + 8
        answer = int(input(f'#{question}: {num1} x {num2} = '))
        if answer != quotient:
            print('Incorrect!\n')
            wrongAnswers += 1
            continue
        if answer == quotient:
            print('Correct!')
            correctAnswers += 1
            break