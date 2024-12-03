import random

# ASCII art representations of Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Dictionary to map choices to their ASCII representations
animation = {0: rock, 1: paper, 2: scissors}
choices = ["Rock", "Paper", "Scissors"]


def print_intro():
    intro_art = r'''
██████╗  ██████╗  ██████╗██╗  ██╗                           
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝                           
██████╔╝██║   ██║██║     █████╔╝                            
██╔══██╗██║   ██║██║     ██╔═██╗                            
██║  ██║╚██████╔╝╚██████╗██║  ██╗                           
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝                           
                                                            
██████╗  █████╗ ██████╗ ███████╗██████╗                     
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗                    
██████╔╝███████║██████╔╝█████╗  ██████╔╝                    
██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗                    
██║     ██║  ██║██║     ███████╗██║  ██║                    
╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                    
                                                            
███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                            
    '''
    print(intro_art)
    print("Welcome to Rock-Paper-Scissors!")


def get_user_choice():
    while True:
        try:
            user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
            if user_input in [0, 1, 2]:
                return user_input
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "Computer wins!"


def print_winner():
    winner_art = r'''
██╗    ██╗██╗███╗   ██╗
██║    ██║██║████╗  ██║
██║ █╗ ██║██║██╔██╗ ██║
██║███╗██║██║██║╚██╗██║
╚███╔███╔╝██║██║ ╚████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
'''
    print(winner_art)


def print_loser():
    loser_art = r'''
██╗      ██████╗ ███████╗███████╗
██║     ██╔═══██╗██╔════╝██╔════╝
██║     ██║   ██║███████╗█████╗  
██║     ██║   ██║╚════██║██╔══╝  
███████╗╚██████╔╝███████║███████╗
╚══════╝ ╚═════╝ ╚══════╝╚══════╝
'''
    print(loser_art)


def print_draw():
    draw_art = r'''
██████╗ ██████╗  █████╗ ██╗    ██╗
██╔══██╗██╔══██╗██╔══██╗██║    ██║
██║  ██║██████╔╝███████║██║ █╗ ██║
██║  ██║██╔══██╗██╔══██║██║███╗██║
██████╔╝██║  ██║██║  ██║╚███╔███╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝                                   
'''
    print(draw_art)


def play_game():
    print_intro()  # Call the intro function

    while True:
        #print("\nChoose your option:")
        user_choice = get_user_choice()
        computer_choice = random.randint(0, 2)

        print("\nYou chose:")
        print(animation[user_choice])
        print("Computer chose:")
        print(animation[computer_choice])

        # Determine and print the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Print corresponding ASCII art
        if result == "You win!":
            print_winner()
        elif result == "Computer wins!":
            print_loser()
        else:
            print_draw()

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
