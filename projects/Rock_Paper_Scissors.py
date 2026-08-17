# # Rock paper and scissor game

# import random

# print("-----Welcome to Rock,Paper and Scissor Game-----")
# print("Rock=1", "Paper=2", "Scisors=3")
# player_score = 0
# computer_score = 0
# computer = random.randint(1, 3)

# player = int(input("Enter your choice::"))
# if player == 1 and computer == 1:
#     print("Draw Try again")
# elif player == 1 and computer == 2:
#     print("Computer won")
#     computer_score += 1
# elif player == 1 and computer == 3:
#     print("You won")
#     player_score += 1
# elif player == 2 and computer == 2:
#     print("Draw Try again")
# elif player == 2 and computer == 1:
#     print("You won")
#     player_score += 1
# elif player == 2 and computer == 3:
#     print("Computer won")
#     computer_score += 1
# elif player == 3 and computer == 3:
#     print("Draw Try again")
# elif player == 3 and computer == 1:
#     print("Computer won")
#     computer_score += 1
# elif player == 3 and computer == 2:
#     print("You won")
#     player_score += 1
# else:
#     print("Please enter a valid choice")

# print(f"Computer score: {computer_score}")
# print(f"Your score:{player_score}")





class student:
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print(self.name)

s=student("Riya")
s.display()
