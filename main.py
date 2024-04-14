import random

# Define the game map
rooms = {
    "start": {
        "description": "You are at the entrance of a dark cave. There are two paths leading further in.",
        "paths": {
            "left": "tunnel",
            "right": "bridge"
        }
    },
    "tunnel": {
        "description": "You are in a narrow tunnel. You can see a faint light ahead.",
        "paths": {
            "forward": "treasure_room",
            "back": "start"
        }
    },
    "bridge": {
        "description": "You are on a rickety bridge overlooking a vast chasm.",
        "paths": {
            "forward": "dragon_room",
            "back": "start"
        }
    },
    "treasure_room": {
        "description": "You have found the treasure room! Congratulations, you win!",
        "paths": {}
    },
    "dragon_room": {
        "description": "You are in a room with a sleeping dragon. Be careful!",
        "paths": {
            "sneak": "treasure_room",
            "run": "bridge"
        }
    }
}

current_room = "start"

def print_room_description(room_name):
    print(rooms[room_name]["description"])

def print_available_paths(room_name):
    available_paths = rooms[room_name]["paths"].keys()
    print("Available paths:", ", ".join(available_paths))

def move_to_room(room_name):
    global current_room
    current_room = room_name
    print_room_description(current_room)
    if current_room == "treasure_room":
        print("You found the treasure! You win!")
        return False
    return True

def play_game():
    print("Welcome to the Adventure Game!")
    print_room_description(current_room)

    while True:
        print_available_paths(current_room)
        user_input = input("Enter your choice: ").lower()

        if user_input == "quit":
            print("Thanks for playing!")
            break

        if user_input in rooms[current_room]["paths"]:
            next_room = rooms[current_room]["paths"][user_input]
            if move_to_room(next_room) is False:
                break
        else:
            print("Invalid input! Try again.")

if __name__ == "__main__":
    play_game()