from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    total_life = 10
elif difficulty == 'hard':
    total_life = 5

found_the_number = False
computers_number = random.randint(1, 101)
while total_life != 0 and not found_the_number:
    guess = int(input("Make a guess: "))
    if guess == computers_number:
        print(f"You got it! The answer was {computers_number}.")
        break
    elif guess > computers_number:
        total_life -= 1
        print("Too high.")
        print("Guess again.")
        print(f"You have {total_life} attempts remaining to guess the number.")
    elif guess < computers_number:
        total_life -= 1
        print("Too low.")
        print("Guess again.")
        print(f"You have {total_life} attempts remaining to guess the number.")

if total_life == 0:
    print("You've run out of guesses, you lose.")
