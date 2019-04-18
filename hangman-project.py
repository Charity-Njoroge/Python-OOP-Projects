import random

# the list of words
my_words = ["hello", "banana", "cartoon", "buzzfeed", "boomerang", "awesome"]
word = random.choice(my_words)
no_of_guesses = 0
count = 0
while no_of_guesses < 6:
    print("I am thinking of a word. Enter a letter that you think is in the "
          "word!")
    guess = str(input())
    if len(guess) != 1:
        print("Enter only one letter!")
    for letter in word:
        if letter == guess:
            count = count + 1
            print("the letter %s occurs %d times in word %s ."
                  % (guess, count, word))
print("You did not guess correctly. The word is %s ." % word)
