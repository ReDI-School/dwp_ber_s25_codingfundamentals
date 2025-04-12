###############################################################
#                                                             #
#                      Exercise 1                             #
#                                                             #
###############################################################
'''
  Google time
  --- By using Google, find a function that gives you current date and time and print the current date and time
'''
#code here 👇
from datetime import datetime

now = datetime.now()
print(now)

###############################################################
#                                                             #
#                      Exercise 2                             #
#                                                             #
###############################################################
'''
   Do you still remember loops?
 - Write a function that counts number of letters in a string you input.
 - The function will have 1 parameter, the string that's letters you want to count.
 - Try both variants - print the result (number of letters in the inputed string) and also save the result to the memory, using return. Try to recall what is the difference between using print and return

'''


#code here 👇
def letters_count_print(input_string):
  count = 0
  for character in input_string:
    # check if the character is a letter
    if character.isalpha():
      count += 1
  
  print(count)

r = letters_count_print("Hi")
print("Value of r:", r)  # None as the function does not return!



def letters_count(input_string):
  count = 0
  for character in input_string:
    # check if the character is a letter
    if character.isalpha():
      count += 1

  return count


c = letters_count("Hello! <3")
print(c)

###############################################################
#                                                             #
#                      Exercise 3                             #
#                                                             #
###############################################################
'''
 ** Using results of function in another function
 - Create a simple function with two parameters that returns their sum.
 - Call the function and save the result into a variable (name of the variable is up to you).
 - Create another function with one parameter that decides if the parameter is divided by 3 and prints appropriate messages
 - Call the second function and use the variable that you created in the b) part as argument.

'''

#code here 👇
def add(a, b):
  return a + b

def divisible_by_three(number):
  return number % 3 == 0


r = add(10, 9)
is_r_divisible_by_three = divisible_by_three(r)
print(r, is_r_divisible_by_three)

r = add(10, 8)
is_r_divisible_by_three = divisible_by_three(r)
print(r, is_r_divisible_by_three)

###############################################################
#                                                             #
#                      Exercise 4 -- Bonus                    #
#                                                             #
###############################################################

# Let's have some fun and implement "Rock, Paper, Scissors"!
'''
Here's what you need to do:
1. Complete the game logic inside the play_game(user_choice) function. The function should determine the outcome of the game based on the user's choice (0 for rock, 1 for paper, and 2 for scissors) and the computer's randomly generated choice.
2. The possible outcomes are as follows:
   - If the user's choice is the same as the computer's choice, it's a "Tie."
   - If the user wins, return "You win."
   - If the computer wins, return "You lose."
3. Test the game by calling the function with different user choices and print the results.

Reminder:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
'''

#code here 👇
import random

def play_game(user_choice):
    # Create a list of possible moves
    options = ["rock", "paper", "scissors"]

    # Get computer's move
    computers_move = random.choice(options)

    if players_move not in options:
        raise Exception(f"{user_choice} is not a valid entry: {options}")

    # Game logic
    if computers_move == players_move:
        print("It's a tie! 👔")
    elif computers_move == "rock":
        if user_choice == "paper":
            print("You win, paper wraps the rock! 🎉")
        else:
            print("You lose.. rock beats the scissors! 😿")
    elif computers_move == "paper":
        if user_choice == "rock":
            print("You lose.. paper wraps the rock! 😿")
        else:
            print("You win, scissors cut the paper! 🎉")
    else:
        if user_choice == "paper":
            print("You lose.. scissors cut the paper! 😿")
        else:
            print("You win, rock breaks the scissors! 🎉")

while True:
    players_move = input("Please enter your move:")
    play_game(players_move)