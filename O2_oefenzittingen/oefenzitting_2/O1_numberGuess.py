# Play a number guessing game with the user.
#   The program starts by generating an integer number in the range 1 to 100.
#   If the user guesses correct the first time, she scores 25 points. For each
#   additional guess, the score is halved.
#   Each time the user guesses with an integer number, the program answers
#   with an indication that her guess is too high, too low or correct.
#   If the input is not a positive integer number, that turn is lost with
#   an error message displayed by the program.

# pseudo code:
# Generate a number in between 1 and 100 to guess.
# Initialize the score to the maximum value of 25.
# initialize to guess to an incorrect value (e.g., -1)

# while the latest guess is not correct and the current score is still positive
#     Ask the user for guess
#     if the latest guess was not a positive number
#         Inform the user that the program only accepts positive numbers as guesses
#     otherwise if the latest guess was less than the number to guess
#         Inform the user that his guess was too low
#     otherwise if the latest guess was higher than the number to guess
#         Inform the user that his guess was too high
#     end
# 
#     if the guess was not correct:
#         Halve the score  
#     end
# end
# 
# if the latest guess was correct
#     Congratulate the user, and show his score
# otherwise
#     Inform the user that he failed, and show the number to guess.
# end

from random import *
correct_number = randint(1,100)
score = 25
number_guess = 0

while number_guess != correct_number and score > 0:

    if number_guess < 0:
        print('only positive integers are allowed')
    elif number_guess < correct_number:
        print('too low')
    elif number_guess > correct_number:
        print('too high')

    if number_guess != correct_number:
        score = score/2

    number_guess = int(input('guess a number: '))

if number_guess == correct_number:
    print('congratulations, your score is: ',score)
else:
    print('you failed, the correct number was: ',correct_number)
