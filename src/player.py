# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return (
            f"\nWelcome {self.name} to this isekai world. You are stading {self.room}\n"
        )

    def player_place(self, place):
        moveAround = getattr(self.room, f"{place}_to")
        if moveAround == None:
            print(f"You have walked into a invisable wall{self.name}. try again.")
        else:
            self.room = moveAround
            print(f"\n{self.room}\n ")

