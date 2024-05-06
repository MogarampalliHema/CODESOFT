import random

def get_user_choice():
    user_choice = input("Welcome to Rock, Paper, Scissors with BLACKBOXAI!\n"
                         "Please enter your choice (rock, paper, or scissors): ").lower()
    if user_choice in ['rock', 'paper', 'scissors']:
        return user_choice
    else:
        print("Invalid input. Please try again.")
        return get_user_choice()

def get_computer_choice():
    computer_choices = ['rock', 'paper', 'scissors']
    return random.choice(computer_choices)

def determine_winner(user_choice, computer_choice):
    print(f"\n- Your selection: *{user_choice}*")
    print(f"- My selection: *{computer_choice}*")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "I win!"

def track_scores(user_score, computer_score):
    print(f"\nYour score: {user_score}")
    print(f"My score: {computer_score}\n")

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(result)
        track_scores(user_score, computer_score)

        play_again = input("Would you like to play another round? (yes/no) ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()