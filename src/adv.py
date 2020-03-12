from room import Room
from player import Player
from map import worldMap

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#


def control():
    print(f"---------- Control --------")
    print(f"[n]- to move north ")
    print(f"[s]- to move south ")
    print(f"[e]- to move east ")
    print(f"[w]- to move west ")
    print(f"[q]- to move quite the game ")
    print(f"[m]- to show map ")
    print(f"[h]- to show control ")


# Make a new player object that is currently in the 'outside' room.

newPlayer = Player(input(f"What is your name player?  "), room["outside"])

print(newPlayer)
control()


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.


# Write a loop that:
while True:

    movement = input(f"\nwhere would you like to move? ===>  ").lower()

    # If the user enters "q", quit the game.
    if movement == "q":
        print(f"Come again to continue your adventure, {newPlayer.name}")
        break

    elif movement in ["n", "s", "e", "w"]:
        newPlayer.player_place(movement)

    elif movement == "h":
        control()

    elif movement == "m":
        worldMap()

    # Print an error message if the movement isn't allowed.
    else:
        print(f"that is a illegal move in the game, try again")
