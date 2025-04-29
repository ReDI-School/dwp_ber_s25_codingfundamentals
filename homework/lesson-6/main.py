'''Exercise A- What is the name of a built-in function in "random" package which can generates random integers?
B- Programming: Using the function in section A, generate 10 integers that are between 1 and 100. Create a list. Call it rand_numbers. Use this list to save the generated integers. Print the list. Calculate the average of the numbers in rand_numbers and display the result. (Feel free to write a function for this calculation.) C- Is there any built-in function in Python that can calculate average of numbers? If "yes" use that function to calculate the average of rand_numbers and display the result. D- Is the result of section B and C the same?'''
# Exercise 1:A
print("\n# Exercise 1:")
print("Built_in function name in Random is: Randint")
# Exercise 1:B
print("\n# Exercise 1:B")
from random import randint

def random_numbers():
    return randint(1,100)

rand_numbers = []
for n in range(10):
    rand_numbers.append(random_numbers())

print("Random 10 Numbers: ", rand_numbers)

#Calculate the Average using a function
print("\n# Calculate the Average using a function")

def calculated_average(numbers):
    return sum(rand_numbers)/ len(rand_numbers)
average = calculated_average(rand_numbers)
print("Average: ",average)

# Exercise 1:C Average Func
print("\n# Exercise 1:C Average Func")

import statistics

average_func = statistics.mean(rand_numbers)
print("Average using mean Function: ", average_func)

# Exercise 1:D
print("\n# Exercise 1:D")

print("Is the result of section B and C the same?: Yes")

  
'''#Exercise 2 - Create a Calculator that can perform four basic operations: addition, subtraction, multiplication, and division! Your program asks the user to input the operation they want to perform and input two numbers. Then it performs the operation and display the result.

Instructions: Write a function for each arithmetic operation (add, subtract, multiply, divide). If the user entered an invalid operation, print an appropriate message to inform them. Your program handles errors (like dividing by zero) and invalid input (like entering a letter instead of a number).'''

# Exercise 2
print("\n# Exercise 2 Four Basic Operations")

def add(x,y):
    return x +y
def subtract( x,y):
    return x - y
def multiply( x,y):
    return x * y
def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Error: Cannot divide br zero."
    
def calculator():
    print("Basic Calculator")
    print("Available operations: add, subtract, multiply, divide")

    operation = input("Enter the operation you'd like to perform: ").strip().lower()

    if operation not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid operation. Please choose from add, subtract, multiply, divide.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)

    print(f"The result of the {operation} operation is: {result}")

# Run the calculator
calculator()


'''Create "Guess the Number" game! Your program generates a random number between 1 and 100. Then asks the user to guess the random number. The user have 5 times to guess the number. If they cannot guess it correctly during this 5 rounds, they loose. Each round that the user guess the number wrong, your program gives the user a hint like "Too low!" or "Too high!". If the guess is correct it should print "Correct!" and prints the number of tries.

Instructions: Write a function to generate a random number. Write a function to ask the user for their guess. Write a function to check if the guess is correct, too high, or too low. Write a main function that loops until the user guesses correctly and provides feedback.'''

# Exercise 3

print("\n# Exercise 3")

import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess(attempt):
    try:
        guess = int(input(f"Attempt {attempt}/5 - Enter your guess (1-100): "))
        if 1 <= guess <= 100:
            return guess
        else:
            print("Please enter a number between 1 and 100.")
            return get_user_guess(attempt)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_guess(attempt)

def check_guess(guess, target):
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

def play_game():
    print("Guess the Number")
    target_number = generate_random_number()
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        guess = get_user_guess(attempt)
        result = check_guess(guess, target_number)

        if result == "Correct!":
            print(f"Correct! You guessed the number in {attempt} tries.")
            return
        else:
            print(result)

    print(f"Sorry, you've used all {max_attempts} attempts. The number was {target_number}.")

# Start the game
play_game()