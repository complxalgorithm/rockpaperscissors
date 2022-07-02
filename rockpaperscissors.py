# Name: rockpaperscissors.py
# Author: Stephen C Sanders <https://stephensanders.me>
# Description: Rock Paper Scissors game. Keeps track of your record again the program, and will output that after session is terminated.

import random          # Required to use randint()

# Main function
def main():
    # Initialize variables
    comp = 4           # Used to 
    user = 5           # Used to 
    comp_choice = 0    # Used to store program's choice
    user_choice = 0    # Used to store user's choice
    comp_score = 0     # Used to keep track of number of games program won
    user_score = 0     # Used to keep track of number of games user won
    ties = 0           # Used to keep track of number of tie rounds
    num_rounds = 0     # Used to keep track of number of rounds played
    cont_status = 'Y'  # Used to ask user if they would like to keep playing

    # Welcoming prompts
    print('Welcome to the Rock Paper Scissors game!')
    input('Click ENTER to continue...')

    # Loop to keep playing until user enters that they want to stop
    while cont_status == 'Y' or cont_status == 'y' or cont_status == 'Yes' or cont_status == 'YES' or cont_status == 'yes':
        comp_choice = get_program_choice()  # Get program's choice
        user_choice = get_user_choice()     # Get user's choice

        who_won = get_winner(comp_choice, user_choice)  # Determine who won the round

        # Output winner of round based on value of who_won variable
        if who_won == 4:
            print('The program wins this round!\n')
            comp_score += 1
        elif who_won == 5:
            print('You win this round!\n')
            user_score += 1
        else:
            print('There was a tie this round!\n')
            ties += 1

        num_rounds += 1  # Add 1 to number of rounds played
        comp_choice = 0  # Reinitialize program's choice
        user_choice = 0  # Reinitialize user's choice

        # Ask user if they would like to continue playing
        cont_status = get_continue_status()

    # Output statistics and goodbye message
    print(f'You played a total of {num_rounds} rounds.')
    print(f'Your record against the program was {user_score}-{comp_score}-{ties}.')
    print('Thank you for playing! I will see you next time.')

# Generate program's choice
def get_program_choice():
    # 1 = Rock; 2 = Paper; 3 = Scissors
    prog = random.randint(1, 3)
    return prog

# Acquire user's choice
def get_user_choice():
    # Get user choice
    choice = input('Enter your choice of rock, paper, or scissors: ')

    # Only specified answers are considered valid
    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return choice
    else:
        print('ERROR: Input was either: not in all lowercase, or was completely invalid. Please try again.')
        return get_user_choice()

# Determine winner of round
def get_winner(prog, user):
    p = ""  # Intialize variable that stores converted program's int choice's string equivalent

    # Assigns p variable string value
    if prog == 1:
        p = "Rock"
    elif prog == 2:
        p = "Paper"
    else:
        p = "Scissors"

    # Output choices
    print(f'Program chose: {p}\nUser chose: {user.capitalize()}')

    # Determine winner and return value to variable in main function
    if (prog == 1 and user == "scissors") or (prog == 2 and user == "rock") or (prog == 3 and user == "paper"):
        return 4  # Program wins
    elif (prog == 1 and user == "paper") or (prog == 2 and user == "scissors") or (prog == 3 and user == "rock"):
        return 5  # User wins
    else:
        return 6 # Tie

# Ask user whether they would like to continue playing or not
def get_continue_status():
    # Get user decision
    inp = input('Would you like to play again? Y or N: ')

    # If input is not any of the options, then the input is invalid
    if inp in ('Y', 'N', 'y', 'n', 'Yes', 'YES', 'yes', 'No', 'NO', 'no'):
        return inp
    else:
        print('ERROR: Invalid input. Try again.')
        return get_continue_status()

# Execute main function
main()
