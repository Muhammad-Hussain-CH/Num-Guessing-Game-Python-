import os # Used to clear the screen

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_secret_number():
    """Gets a valid secret number from Player One."""
    while True:
        try:
            secret_num = int(input("Player One, enter a secret number (between 1 and 100): "))
            if 1 <= secret_num <= 100:
                return secret_num
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def play_guessing_game(secret_num):
    """Handles Player Two's guessing turn."""
    attempts = 0
    while True:
        try:
            guess = int(input("Player Two, guess the number: "))
            attempts += 1
            if guess == secret_num:
                print(f"\nCongratulations, Player Two! You guessed the number {secret_num} in {attempts} attempts.")
                break
            elif guess < secret_num:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    print("Welcome to the 2-Player Number Guessing Game!")

    secret_number = get_secret_number()

    # Clear the screen to hide the secret number from Player Two
    clear_screen()
    print("Screen cleared. Player Two, it's your turn to guess!")

    play_guessing_game(secret_number)

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()