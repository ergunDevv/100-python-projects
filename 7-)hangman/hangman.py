import random
import hangman_art
import hangman_words
stages = hangman_art.stages

end_of_game = False
lives = 6

word_list = hangman_words.word_list
display = []
is_player_found_the_letter = False
chosen_word = random.choice(word_list)

used_letters = []
print(hangman_art.logo)
for n in range(0, len(chosen_word)):
    display.append('-')

while '-' in display and lives != 0:
    guess = input("Guess a letter: ").lower()
    if guess in used_letters:
        print('You already used this letter')
        lives -= 1
        print(stages[lives])

        continue
    else:
        used_letters += guess

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            is_player_found_the_letter = True
            display[i] = guess
    print(display)
    print(stages[lives])
    if "-" not in display:
        end_of_game = True
        print(f"{' '.join(display)}")
        print("You win.")
    if is_player_found_the_letter == False:
        print('Word doesnt include this letter.')
        lives -= 1
    is_player_found_the_letter = False

if lives == 0:
    print(stages[lives])
    print('You lose!')
