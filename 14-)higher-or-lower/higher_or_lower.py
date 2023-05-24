import art
import game_data
import random
game_over = False
final_score = 0


def select_the_influencer():
    first_inf = random.choice(game_data.data)
    second_inf = random.choice(game_data.data)
    print(art.logo)
    if final_score != 0:
        print(f"You're right! Current score: {final_score}.")
    print(
        f"Compare A: {first_inf['name']} , {first_inf['description']} , {first_inf['country']}")
    print(art.vs)
    print(
        f"Compare B: {second_inf['name']} , {second_inf['description']} , {second_inf['country']}")
    who_is_winner = input("Who has more followers? Type 'A' or 'B': ").lower()
    real_winner = ''
    if first_inf['follower_count'] > second_inf['follower_count']:
        real_winner = 'a'
    else:
        real_winner = 'b'
    return real_winner, who_is_winner


while not game_over:
    real_winner, who_is_winner = select_the_influencer()
    if who_is_winner == real_winner:
        final_score += 1

    else:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        game_over = True
