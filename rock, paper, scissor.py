import random

options=["Rock", "Paper", "Scissors"]

#Take user input 
user_choice=input("Choose Rock, Paper, or Scissors:")

#Generate computer's choice 
computer_choice=random.choice(options)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

#Determine the winner
if user_choice == computer_choice:
    print("It's a tie!!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")
else:
    print("Computer wins!")                