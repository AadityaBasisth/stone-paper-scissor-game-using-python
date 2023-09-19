# Creating a game of stone, paper and scissor in Python of Player vs Computer type
''' Rules of the game are as follows:
stone vs paper : paper wins
stone vs scissor : stone wins
paper vs scissor : scissor wins
'''
# Using the random module to generate computers choice
import random
print("computer is selecting")
computer_choice=random.randint(1,3)
print("The computer has selected its choice.")

# asking the user to enter the choice, the choice entered is case insensitive, user can  enter capital as well as small case letter.
user_choice=input("Enter your choice : Stone🥌(s)   Paper📄(p)    Scissor✂(c) :    ")

# Asking corresponding values to user choice along with displaying the input chosen by the user.
if user_choice=="s" or user_choice=="S":
    print("you chose stone🥌.")
    user_choice=1
elif user_choice=="p" or user_choice=="P":
    print("you chose paper📄.")
    user_choice=2
elif user_choice=="c" or user_choice=="C":
    print("you chose scissor✂.")
    user_choice=3
else:
    print("Enter a valid choice")


# Showing the computers choice
if computer_choice==1:
    print("Computer chose stone🥌.")
elif computer_choice==2:
    print("Computer chose paper📄.")
else:
    print("Computer chose scissor✂.")


# Creating the possible cases of the game

# If both chose same, game is a draw
if user_choice==computer_choice:
    print("Its a tie🙂")



# If user chooses stone, the possible cases except for draw
if user_choice==1:
    if computer_choice==2:
        print("you lose😫")
    elif computer_choice==3:
        print("you win😊")


# If user chooses paper, the possible cases except for draw
if user_choice==2:
    if computer_choice==1:
        print("you win😊")
    elif computer_choice==3:
        print("you lose😫")


# If user chooses scissor, the possible cases except for draw
if user_choice==3:
    if computer_choice==1:
        print("you lose😫")
    elif computer_choice==2:
        print("you win😊")
