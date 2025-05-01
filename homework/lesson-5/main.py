# Exercises on Functions and Imports
#Homework 1:Google Time
print("\n#Homework 1:Google Time")
import datetime
current_date_and_time = datetime.datetime.now()
print(" # current Date & Time: ",current_date_and_time)

#Homework 2: Function to print Letters in a parameter
print("\n#Homework 2: Function to print Letters in a parameter")
# Print vowel Letters


def count_vowel_letters(text):
    count = 0
    vowel_sounds = "aeiou"
    for i in text:
        if i in vowel_sounds:
            count += 1
    return count
text = input("Type text: ")

count = count_vowel_letters(text)

print(" Count: ", count)


# Homework 3: Using results of a function in another function
print("\n# Homework 3: Using results of a function in another function")
def sum_of_x_and_y(x ,y):
    print(x +y)
    total = x + y
    return total
sum_of_x_and_y(4,2)

def divisible_by_3(total, ):
    if total % 3 == 0:
        print("Number is divisible by 3")
    else:
        print("Number is not divisivle by 3")
total = sum_of_x_and_y(4,2)
divisible_by_3(total)

# Homework 4: Rock Paper Scissors
print("\n# Homework 4: Rock Paper Scissors")
import random
def play_game(user_choice,):
    choices = ("rock", "paper" "scissors")
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
             print("It's a Tie")
    elif user_choice == 0 and computer_choice == 2:
            print("You Win")
    elif user_choice == 2 and computer_choice == 1:
         print("You Win")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win")
    else:
        print("You Lose")
while True:
    player_move = input("Enter your move: ")
    play_game(player_move)
    

'''# Rock Paper Scissors Game with Input function
import random
choices = ("rock = 0", "paper = 1", "scissors = 2")
user_choice = input("Type in your choice: ")
computer_choice = random.choice(choices)
def play_game(user_choice, computer_choice):
    return computer_choice
outcome = play_game(user_choice, computer_choice)
print(outcome)
if user_choice == computer_choice:
             print("It's a Tie")
elif user_choice == 0 and computer_choice == 2:
            print("You Win")
elif user_choice == 2 and computer_choice == 1:
         print("You Win")
elif user_choice == 1 and computer_choice == 0:
        print("You Win")
else:
        print("You Lose")
play_game(user_choice, computer_choice)'''










