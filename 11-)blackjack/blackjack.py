from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def choose_random_card():
    card = random.choice(cards)
    return card


def start_game():
    player = []
    computer = []
    total_player_score = 0
    total_computer_score = 0
    print(logo)
    # Initial
    player.append(choose_random_card())

    def draw_card(total_player_score, total_computer_score):
        player.append(choose_random_card())
        computer.append(choose_random_card())
        total_player_score = sum(player)
        total_computer_score = sum(computer)
        return total_player_score, total_computer_score
    def draw_card_for_computer( total_computer_score):
        computer.append(choose_random_card())
        total_computer_score = sum(computer)
        return  total_computer_score
    
    def check_score_for_player():
        if total_player_score >= 21:
            return True
        return False

    def check_score_for_computer():
        if total_computer_score >= 21:
            return True
        return False
    def check_result(total_player_score, total_computer_score):
        if total_computer_score==total_player_score:
            print('Draw!')
        elif total_player_score==21:
            print("Win with a Blackjack 😎")
        elif total_computer_score==21:
            print(" Lose with a Blackjack 😤")
        elif total_player_score>21:
            print("You went over. You lose 😤")
        elif total_computer_score>21:
            print("Opponent went over. You win 😁")
        elif total_computer_score>total_player_score:
            print("You lose 😤")
        elif total_player_score>total_computer_score:
            print("You win 😃")

        
        
    total_player_score, total_computer_score = draw_card(
        total_player_score, total_computer_score)
    print(f"Your cards: {player}, current score: {total_player_score}")
    print(f"Computer's first card: {total_computer_score}")
    if total_player_score>=21 or total_computer_score>=21:
        print()
    else:

    
        continue_draw_card = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        

        while not check_score_for_computer() and not check_score_for_player() :
            if total_player_score>=21 or total_computer_score>=21:
                break
            if continue_draw_card=='y':
                total_player_score, total_computer_score = draw_card(
                total_player_score, total_computer_score)
            else:
                total_computer_score = draw_card_for_computer(
                total_computer_score)
            if total_player_score>=21 or total_computer_score>=21:
                break       
            print(f"Your cards: {player}, current score: {total_player_score}")
            print(f"Computer's first card: {computer[0]}")
            continue_draw_card = input(
                "Type 'y' to get another card, type 'n' to pass: ")
    print(f"Your final hand: {player}, final score: {total_player_score}")
    print(f"Computer's final hand: {computer}, final score: {total_computer_score}")
    check_result(total_player_score, total_computer_score)
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
        start_game()

if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    start_game()

