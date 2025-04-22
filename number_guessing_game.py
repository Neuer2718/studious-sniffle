import random  # Import the random module to generate a random number

# Define the main game logic in a function
def play_game():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  # Counter for number of guesses
    max_attempts = 10  # Maximum number of allowed guesses

    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    print(f"You have {max_attempts} attempts.\n")

    # Main guessing loop
    while attempts < max_attempts:
        try:
            guess = int(input('Enter your guess: '))  # Get user input and convert to integer
            attempts += 1  # Increment the attempts counter
            remaining = max_attempts - attempts  # Calculate remaining attempts

            # Check if guess is within valid range
            if guess < 1 or guess > 100:
                print("Please guess a number *within* the range 1 to 100.")
                continue  # Skip the rest of the loop and prompt again

            # Calculate the difference to give a hint later
            difference = abs(number_to_guess - guess)

            # Compare guess to the target number
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                # Correct guess
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop

            # Provide proximity hints
            if difference <= 5:
                print("🔥 You're very close!")
            elif difference <= 10:
                print("🌡️ You're getting warm.")
            else:
                print("❄️ Cold.")

            # Tell the user how many guesses remain
            if remaining > 0:
                print(f"You have {remaining} {'attempt' if remaining == 1 else 'attempts'} left.\n")
            else:
                # No attempts left
                print(f"\n🚫 Game Over! The number was {number_to_guess}.")

        except ValueError:
            # Handle non-integer input gracefully
            print("⚠️ Please enter a valid number.\n")

# This function handles replay logic
def main():
    while True:
        play_game()  # Play one round of the game
        again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Thanks for playing! 👋")
            break  # Exit the loop if user says no
        print("\nStarting a new game...\n")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()