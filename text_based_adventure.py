""" A program that  let users move through rooms based on user input
and get descriptions of each room
exercise: store data in a text file, use the csv module; add creatures and
points to score
"""

# room information and direction
rooms = {"King's Landing": {"name": "The King's Landing", "west": "Temple",
                            "north": "The Wall", "contents": [],
                            "description": "Welcome to the Kings Landing."
                                           "The throne is made of swords!"},
         "Temple": {"name": "the temple", "east": "King's Landing",
                    "north": "Dothraki", "contents": ['benches', 'cross'],
                    "description": "You are at the temple! Say a prayer if"
                                   " you may!"},
         "The Wall": {"name": "the wall", "west": "Dothraki",
                      "south": "King's Landing", "contents": [],
                      "description": "Ice! Winter is here!"},
         "Dothraki": {"name": "the Dothraki Kingdom", "east": "The Wall",
                      "south": "Temple",
                      "contents": ['Khaleesi', 'swords'],
                      "description": "Here we have dragon"
                                     "eggs and Karl Drogo!"}}

directions = ["north", "east", "south", "west"]
# set current room to King's Landing
current_room = rooms["King's Landing"]
carrying = []

# game loop
while True:
    print()
    print("The room you are in is {}.".format(current_room['name']))
    print(current_room['description'])
    print()
    if current_room['contents']:
        print("The contents of the current room are {}.".format(
            current_room['contents']))
        print()
    print("Choose the direction to move: Allowed directions are north, east,"
          "south, and west. You can also choose quit or q to end the game")
    print()
    command = input("").strip()
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            print("Invalid move!")

    elif command in ('q', 'quit'):
        break

    else:
        print("I don't understand that command!")

