# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
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

# Write your code below this line 👇
player_decision = rock
random_num = random.randint(0, 2)
if random_num == 0:
    computer_ = rock
if random_num == 1:
    computer_ = paper
if random_num == 2:
    computer_ = scissors

player = input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')

if player == 0:
    player_decision = rock
if player == 1:
    player_decision = paper
if player == 2:
    player_decision = scissors

if player_decision == rock and computer_ == scissors:
    print('You won!')
if player_decision == rock and computer_ == paper:
    print('You lose!')
if player_decision == scissors and computer_ == rock:
    print('You won!')
if player_decision == scissors and computer_ == paper:
    print('You lose!')

if player_decision == paper and computer_ == rock:
    print('You lose!')
if player_decision == paper and computer_ == scissors:
    print('You won!')
