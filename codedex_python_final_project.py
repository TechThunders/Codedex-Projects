import random as r 
import time as t
import pywriter as p
import os as o

hangman_art = """
====================================================================================================

    HHH    HHH     AAA     NNNNNN    NNN    GGGGGG MMMMMM       MMMMMM     AAA     NNNNNN    NNN
    HHH    HHH    AA AA    NNN NNN   NNN  GGG      MMM MMM     MMM MMM    AA AA    NNN NNN   NNN
    HHHHHHHHHH   AAAAAAA   NNN  NNN  NNN GGG   GGG MMM  MMM   MMM  MMM   AAAAAAA   NNN  NNN  NNN
    HHH    HHH  AAA   AAA  NNN   NNN NNN  GGG   GG MMM   MMM MMM   MMM  AAA   AAA  NNN   NNN NNN
    HHH    HHH AAA     AAA NNN    NNNNNN    GGGGGG MMM    MMMMMM   MMM AAA     AAA NNN    NNNNNN

====================================================================================================


"""

wel_msg = """Welcome to the Game of Hangman.
It is a game for two players, where one enters the word and the other tries to guess it.
You have 5 lives. If you succeed, congrats; if you lose, better luck next time.

For your info:
1. The letters can be upper-case or lower-case, enter as it was entered by other person.
2. Hints are only available if they are allowed by the other person.
3. You are only allowed to enter letter by letter, not whole word or part of it
"""

hangman = ["""
_______
|     
|
|
|
|\n\n""", """
________
|      |
|    
|     
|      
|\n\n     """, """
________
|      |
|    <( )>
|     
|      
|\n\n     """, """
________
|      |
|    <( )>
|     /T\\
|      
|\n\n      """, """
________
|      |
|    <( )>
|     /T\\
|      |
|\n\n       """, """
________
|      |
|    <( )>
|     /T\\
|      |
|     /|\\ \n\n"""]

word = ""
hint1 = "" 
hint2 = ""
hint3 = ""
hint_given = False
word_list = []
dash_list = []
not_allowed_again = []
display_list = dash_list.copy()
lives = 5
hangman_display = 5 - lives
hint_counter = 1
chances = [1,2,3,4]
kk = r.choice(chances)
finished = False
index = 0
word_guessed = False
hints_printed = False

def clear_screen():
    o.system('cls' if o.name == 'nt' else 'clear')

clear_screen()

p.write(hangman_art)
p.write(wel_msg)

word = input("\n\nWhat is your word: ")
hint_yn = input("Do you want to allow hints (Y/N): ")

if hint_yn.upper() == "Y":
    hint_given = True
    hint1 = input("Enter the 1st hint: ")
    hint2 = input("Enter the 2nd hint: ")
    hint3 = input("Enter the 3rd hint: ")

clear_screen()

for i in word:
    dash_list.append("_")
    display_list = dash_list.copy()

p.write(hangman_art)
p.write("Ok, Now its the turn of the other player.")
p.write(hangman[hangman_display])


for i in word:
    word_list.append(i)

letters = r.choices(word_list, k = kk)
letters.append(" ")

while hints_printed == False:
    if len(letters) == 0:
        hints_printed = True
    elif letters[0] in word_list:
        for i, ch in enumerate(word_list):
            if ch == letters[0]:
                display_list[i] = letters[0]
        not_allowed_again.append(letters[0])
        letters.pop(0)
    else:
        letters.pop(0)

p.write("Lives left: " + str(lives))
p.write(display_list)

while word_guessed == False:
    guess_letter = input("Enter your guess or enter 'Hint' for a hint if hints are enabled by other person: ")
    if guess_letter.lower() == "hint" and hint_given == True:
        if hint_counter == 1:
            hangman_display = 5 - lives
            p.write(hangman[hangman_display])
            p.write("Lives left: " + str(lives))
            p.write(display_list)
            p.write("\nHint 1: " + hint1)
            hint_counter += 1
        elif hint_counter == 2:
            hangman_display = 5 - lives
            p.write(hangman[hangman_display])
            p.write("Lives left: " + str(lives))
            p.write(display_list)
            p.write("\nHint 2: " + hint2)
            hint_counter += 1
        elif hint_counter == 3 and lives == 1:
            hangman_display = 5 - lives
            p.write(hangman[hangman_display])
            p.write("Lives left: " + str(lives))
            p.write(display_list)
            p.write("\nHint 3: " + hint3)
            hint_counter += 1
        elif hint_counter == 3 and lives != 1:
            p.write("Sorry, but 3rd hint is only available on last life.")
        elif hint_counter > 3:
            p.write("All hints are used.")


    elif hint_given == False and guess_letter.lower() == "hint":
        p.write("Sorry but hints are not enabled")


    if guess_letter in not_allowed_again:
        hangman_display = 5 - lives
        p.write(hangman[hangman_display])
        p.write("Lives left: " + str(lives))
        p.write(display_list)
        p.write("Already in the word!")


    elif guess_letter in word_list and not guess_letter.lower() == "hint":
        hangman_display = 5 - lives
        for i, ch in enumerate(word_list):
            if ch == guess_letter:
                display_list[i] = guess_letter
        p.write(hangman[hangman_display])
        p.write("Lives left: " + str(lives))
        p.write(display_list)
        not_allowed_again.append(guess_letter)

    elif guess_letter not in word_list and guess_letter not in not_allowed_again and guess_letter.lower() != "hint":
        lives = lives - 1
        hangman_display = 5 - lives
        p.write(hangman[hangman_display])
        p.write("Lives left: " + str(lives))
        p.write(display_list)
        p.write("Wrong Answer!")

    if lives == 0:
        p.write("You Lost! the word was " + word + "." )
        break

    if "".join(display_list) == word:
        p.write("You Won! 🥳🥳")
        word_guessed = True