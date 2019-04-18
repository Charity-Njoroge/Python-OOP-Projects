""" A program that generates a random integer and asks
a user to guess it and gives the user hints when they enter wrong guess """
import random


class CustomError(Exception):
    """ A base class for the classes that handles exceptions"""
    pass


class ValueTooSmallError(CustomError):
    """ A class to handle value too small error"""
    pass


class ValueTooLargeError(Exception):
    """ A class to handle value too large error """
    pass


number = random.randint(1, 20)
print("Hey there! I am thinking of a number between 1 and 20.")
number_of_guesses = 0
while number_of_guesses < 6:
    try:
        print("Can you guess it \n")
        guess = int(input())
        number_of_guesses = number_of_guesses + 1

        if guess > number:
            raise ValueTooLargeError
        elif guess < number:
            raise ValueTooSmallError
        break
    except ValueTooLargeError:
        print("The guess was too large. Guess a smaller number.")
        print()

    except ValueTooSmallError:
        print("The guess was too small. Guess a larger number.")
        print()

if guess == number:
    print("You guessed correctly after %d guesses! The number is %d " %
          (number_of_guesses, number))
elif guess != number:
    print("You did not guess correctly! The number is %d" % number)
