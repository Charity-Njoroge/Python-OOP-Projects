import random


guessesTaken = 0

print("Enter name")
name = input()
print("Hello " + name + " welcome to my game. Guess a number between 1 and 20")
number = random.randint(1, 20)
while guessesTaken < 6:
    print("Take a guess")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken - 1

    if guess < number:
        print("guess is too small")
    elif guess > number:
        print("guess is too big")
    elif guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print("You guessed correctly! After " + guessesTaken + " guesses")

if guess != number:
    number = str(number)
    print("Nope! The number i was thinking of is" + number)

print()
