import random as rd
with open('wordList.txt', 'r') as f:
    words = f.readlines()

word = rd.choice(words)[:-1]

guesses = []
allowed_guesses = 7
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Number of lives left: {allowed_guesses}, guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_guesses -= 1
        if allowed_guesses == 0:
            break
    
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word! It was {word}!")
else:
    print("Game Over! The word was {word}!")
