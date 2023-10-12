import random
from hangman_words import generate_word_list
from hangman_art import logo, stages

level = 0
while level not in [1, 2, 3]:
    level = int(input("Choose the level of hardness: \n(1) Easy, \n(2) Medium, \n(3) Hard: \nLevel?:"))

if level == 1:
    word_length = 4
elif level == 2:
    word_length = 6
elif level == 3:
    word_length = 8

end_of_game = False
lives = 6

print(logo)

word_list = generate_word_list()
chosen_word = random.choice([word for word in word_list if len(word) == word_length])
display = [chosen_word[0]] + ["_"] * (word_length - 2) + [chosen_word[-1]]

print(' '.join(display))  # Show the initial display with the first and last letters revealed

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The chosen word was: {chosen_word}")

    print(' '.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
