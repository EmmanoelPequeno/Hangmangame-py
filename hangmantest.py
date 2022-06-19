#list of words
#show th

import random
import string

print("oi)

#funcs
def verifyOneLetter(lenght):
    if lenght > 1:
        print("Write just one letter!")
    else:
        return False

def isALetter(value):
    possible_letters = list(string.ascii_lowercase)
    if value in possible_letters:
        return
    else:
        print("It's not a letter, please wirte one")

#code
possible_words = ["hangman", "python", "java", "kotlin", "javascript", "reference", "programing", "freelancer", "bug", "wrong"]
word_chose = random.choice(possible_words)
print(f"your word has {len(word_chose)} letters")
word_show = list(("_"*len(word_chose)))
count_finish = len(word_chose)
count_lifes = len(word_chose)-1

#input just one letter
while count_finish != 0:
    print(word_show)
    letter_guess = input("Guess a letter: ")
    verifyOneLetter(len(letter_guess))
    isALetter(letter_guess)

    if letter_guess in word_chose:
        for letter in range(len(word_chose)):
            if letter_guess == word_chose[letter]:
                word_show.pop(letter)
                word_show.insert(letter, letter_guess)
                count_finish = count_finish -1
            else:
                count_lifes -1
print(word_show)
print("Parabéns, você chegou ao final do game!!")
