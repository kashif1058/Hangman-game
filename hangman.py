import random
# import hangman_art
from hangman_art import logo, stages
import hangman_words
from hangman_words import word_list

end_of_game = False

lives = 6
# word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
print(logo)
# Testing Code
# 

display  = []
for _ in range(word_length):  
  display += "_"
  # display = display  + "_"
print(display)

while not end_of_game:
  guess = input("Guess a  letter: ").lower() 
  if guess in display:
    print(f"You have already guessed {guess}") 
  for position in range(word_length):  
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)

  if "_" not in display:
    end_of_game = True
    print("You Won!")

  if guess not in chosen_word:
    # 4 -1 = 3
    lives = lives - 1
    print(f"you have left with {lives} lives")
    if lives == 0:
      end_of_game = True
      print("You Lose!")
      print(f"The chosen word was: {chosen_word}")

  print(stages[lives])