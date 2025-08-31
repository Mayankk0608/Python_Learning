# snake vs water = water wins         snake beats water but loses to gun 
# gun vs snake = gun wins             gun beats snake but loses to water 
# water vs gun = water wins           water beats gun but loses to snake 
# if both choose same the game is tie

import random

def snake_water_gun():
    choice = ["snake", "water", "guns"]

    user_choice = input("Enter your choice(snake , water and guns): ").strip().lower()
    if user_choice not in choice:
        return "Invalid choice from user !!! You have to select from snake , water and guns... "

    computer_choice = random.choice(choice)


    print(f"Your choice: {user_choice}")
    print(f"computer choice: {computer_choice}")

    if user_choice == computer_choice:
        return "its a tie"
    
    elif user_choice == "snake" and computer_choice == "water" or \
         user_choice == "guns" and computer_choice == "snake" or \
         user_choice == "water" and computer_choice == "guns":
         return "You win"
    
    else:
        return "Computer win"
    
print(snake_water_gun())