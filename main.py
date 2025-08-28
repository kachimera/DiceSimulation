import random
import time


def roll_dice():
    print("🎲 Rolling the dice...")
    time.sleep(1)  # Adds a small delay for realism

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print(f"🟦 You rolled: {die1} and {die2}")
    print(f"🔢 Total: {die1 + die2}\n")


# Main game loop
def main():
    print("🎮 Welcome to Dice Roller!")

    while True:
        user_input = input("Press Enter to roll or type 'q' to quit: ").lower()
        if user_input == 'q':
            print("👋 Thanks for playing. Goodbye!")
            break
        roll_dice()


main()
