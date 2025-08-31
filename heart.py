import random

def rock_paper_scissor():
    choices = ["rock","paper","scissors"]

    user_choice = (input("Enter your choice (rock , paper and scissors): ")).strip().lower()
    if user_choice not in choices:
        return "Invalid choice from user !!! You have to select from rock , paper and scissors... "

    computer_choice = random.choice(choices)

    print(f"Your choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        return "Its a tie !!"
    
    elif user_choice == "rock" and computer_choice == "scissors" or \
         user_choice == "paper" and computer_choice == "rock" or \
         user_choice == "scissors" and computer_choice == "paper":
        return "You win !!"
    
    else:
        return "Computer win !!"
    
print(rock_paper_scissor())