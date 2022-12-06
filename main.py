import random
from hangman_art import * 
from hangman_words import word_list

lives = 6

words_list = word_list

random_word = random.choice(word_list)


display = []

for i in random_word:
    display += "_"
    
# GAME START GROUP
print(logo)
print("Welcome to hangman!")
print("".join(display))
print(" ")
user_guess = input("Guess a letter. ").lower()


word_length = len(random_word)

while "_" in display:
    for index in range(word_length):          
        if random_word[index] == user_guess:
            display[index] = random_word[index]
    if "_" in display:
        if user_guess not in display:
            print("Wrong guess, try again!")
            lives -= 1
            if lives == 0:
                print(stages[lives])
                print("You Lose")
                break
        print(stages[lives])
        print("".join(display))
        print(" ")
        user_guess = input("Guess a letter. ").lower()
    else: 
        print("".join(display))
        print("You Win")
        