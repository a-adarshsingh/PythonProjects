"""
Text Adventure Game — small room-based exploration game with inventory and a win condition.
"""

ROOMS = {
    "hall": {
        "description": "You are in a dusty entrance hall. Exits: north, east.",
        "exits": {"north": "library", "east": "kitchen"},
        "item": None,
    },
    "library": {
        "description": "Shelves of old books line the walls. Exits: south.",
        "exits": {"south": "hall"},
        "item": "brass key",
    },
    "kitchen": {
        "description": "An old kitchen, cold and empty. Exits: west, down.",
        "exits": {"west": "hall", "down": "cellar"},
        "item": "rusty knife",
    },
    "cellar": {
        "description": "A dark cellar. There is a locked door to the east. Exits: up, east.",
        "exits": {"up": "kitchen", "east": "treasure_room"},
        "item": None,
    },
    "treasure_room": {
        "description": "Sunlight glints off a pile of gold. You win!",
        "exits": {},
        "item": None,
    },
}


def play():
    current = "hall"
    inventory = []
    print("=== The Old Manor ===")
    print("Commands: go <direction>, take, inventory, quit\n")

    while True:
        room = ROOMS[current]
        print(f"\n{room['description']}")
        if room["item"]:
            print(f"You see a {room['item']} here.")

        if current == "treasure_room":
            print("\nCongratulations, you found the treasure! You win!")
            break

        command = input("\n> ").strip().lower()

        if command == "quit":
            print("Thanks for playing!")
            break

        elif command == "inventory":
            print("You are carrying:", ", ".join(inventory) if inventory else "nothing")

        elif command == "take":
            if room["item"]:
                inventory.append(room["item"])
                print(f"You took the {room['item']}.")
                room["item"] = None
            else:
                print("There's nothing to take here.")

        elif command.startswith("go "):
            direction = command[3:].strip()
            if direction in room["exits"]:
                dest = room["exits"][direction]
                if dest == "treasure_room" and "brass key" not in inventory:
                    print("The door is locked. You need a key.")
                else:
                    current = dest
            else:
                print("You can't go that way.")

        else:
            print("Unknown command. Try: go <direction>, take, inventory, quit")


if __name__ == "__main__":
    play()
