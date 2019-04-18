"""
program prompts user for a series of inputs a la Mad Libs.
Once all the information has been inputted, the program will take that data
and place them into a pre-made story template
"""

noun1 = str(input("Enter a noun and press enter \n"))
noun2 = str(input("Enter another noun and press enter \n"))
adjective = str(input("Enter an adjective and press enter \n"))

print("A rose is very " + adjective)
print("A " + noun1 + " is very " + adjective)
print("A " + noun1 + " is very " + adjective + " not like " + noun2)

