import random
import time

dice_art = {
    1: ("┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"),
    2: ("┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"),
    3: ("┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"),
    4: ("┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"),
    5: ("┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"),
    6: ("┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"),
}

def print_dice(die1, die2):
    for line1, line2 in zip(dice_art[die1], dice_art[die2]):
        print(f"{line1}   {line2}")

while True:
    choice = input('Roll the dice? (y/n): ').strip().lower()
    if choice == 'y':
        print("Rolling...", end="\r")
        time.sleep(0.8)
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print_dice(die1, die2)
        print(f"You rolled a total of {die1 + die2}!\n")
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print("Invalid choice! Please enter 'y' to roll or 'n' to quit.\n")