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
import random

rock_paper_scissors = ["rock", "paper", "scissors"]
print("welcome to official Rock Paper Scissors game")

human_hand = input("what do you choose? \n rock paper scissors ").lower()
computer_hand = random.choice(rock_paper_scissors)

#human
print("You choose: ")
if human_hand == "rock":
    print(rock)
elif human_hand == "paper":
    print(paper)
elif human_hand == "scissors":
    print(scissors)

#computer
print("computer choose: ")
if computer_hand == "rock":
    print(rock)
elif computer_hand == "paper":
    print(paper)
elif computer_hand == "scissors":
    print(scissors)

#how to function
if computer_hand == human_hand:
    print("it's a draw")
elif computer_hand != human_hand:
    if human_hand == "rock" and computer_hand == "paper":
        print("Paper wins")
    elif human_hand == "rock" and computer_hand == "scissors":
        print("Rock wins")
    elif human_hand == "paper" and computer_hand == "scissors":
        print("Scissors wins")

else:
    print("draw")