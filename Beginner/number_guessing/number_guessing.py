import random

logo = """
 ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5


def get_difficulty():
    while True:
        game_level = input("Choose difficulty: type 'easy' or 'hard': ").lower()
        if game_level in ['easy', 'hard']:
            return EASY_LEVEL_GUESSES if game_level == 'easy' else HARD_LEVEL_GUESSES
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")


def get_guess():
    while True:
        guess = int(input("Make a guess (between 1 and 100): "))
        if 1 <= guess <= 100:
            return guess
        else:
            print("Please enter a number between 1 and 100.")


def play_game():
    the_number = random.randint(1, 100)
    num_of_guesses = get_difficulty()

    while num_of_guesses > 0:
        print(f"You have {num_of_guesses} attempts remaining to guess the number.")
        guess = get_guess()
        num_of_guesses -= 1

        if guess == the_number:
            print(f"You got it! The answer was {the_number}.")
            return True
        elif guess > the_number:
            print("Too high. Guess again.")
        else:
            print("Too low. Guess again.")

    print(f"You've run out of guesses. The number was {the_number}.")
    return False


def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")


if __name__ == "__main__":
    main()
