import random

words = ["Specialization", "Fuzzification", "Synchronization", "Inspiration", "Authorization"]
chosen_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("_ " * len(chosen_word))

while wrong_guesses < max_wrong_guesses:
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())

    if "_" not in display_word:
        print("Congratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! Remaining attempts: {max_wrong_guesses - wrong_guesses}")

if wrong_guesses == max_wrong_guesses:
    print(f"Game Over! The word was '{chosen_word}'.")