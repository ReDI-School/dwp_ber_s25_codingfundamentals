# Import the required modules
import random  # For generating random numbers
import statistics  # For calculating averages using built-in method


print("===================== Exercise 1 =====================")
# Exercise 1

# A: What is the name of a built-in function in "random" package which can generates random integers?
print("A: Function to generate random integers is random.randint(a, b)")

# B: Programming: Using the function in section A, generate 10 integers that are between 1 and 100. 
# Create a list. Call it rand_numbers. 
# Use this list to save the generated integers. 

# Function to generate random numbers
# min_num and max_num: the range of numbers between which a random number is generated
# the default value of min_num is 1
# the default value of max_num is 100
def generate_random_numbers(min_num=1, max_num=100):
    rand_numbers = [] # create the rand_numbers list
    for i in range(0, 10): # for loop to iterate 10 times to generate 10 random numbers
        rand_num = random.randint(min_num, max_num) # generate random number between min_num and max_num
        rand_numbers.append(rand_num)
    return rand_numbers # return the list with all the random numbers

# Print the list. 
random_numbers = generate_random_numbers()
print("B: Random Numbers:", random_numbers)

# Bonus: generating random numbers between 101 and 200
random_numbers_101_200 = generate_random_numbers(min_num=101, max_num=200)
print("10 Random numbers between 101 and 200: ", random_numbers_101_200)

# Calculate the average of the numbers in rand_numbers and display the result. 
# (Feel free to write a function for this calculation.) 

# Function to calculate average using basic math
def calculate_average_1(numbers):
    total = 0 # define a variable to save the total of all the numbers in the list
    
    for num in numbers: # loop through each number in the list
        total += num # add the number to total
    
    average = total / len(numbers) # calculate average
    return average # return average of all the numbers in the list

# Alternate solution using sum()
def calculate_average_2(numbers):
    return sum(numbers) / len(numbers)

average_1 = calculate_average_1(random_numbers)
print("B: Average function 1:", average_1)

average_2 = calculate_average_2(random_numbers)
print("B: Average function 2:", average_2)


# C: Is there any built-in function in Python that can calculate average of numbers? 
# If "yes" use that function to calculate the average of rand_numbers and display the result.

average_builtin = statistics.mean(random_numbers)
print("C: Average (built-in statistics.mean):", average_builtin)

# D: Is the result of section B and C the same?

print("Are the results of section B and C the same?", average_1 == average_builtin)


print("===================== Exercise 2 =====================")
# Exercise 2 - Calculator

# Create a Calculator that can perform four basic operations: 
# addition, subtraction, multiplication, and division! 
# Your program asks the user to input the operation they want to perform and input two numbers. 
# Then it performs the operation and display the result.

# Instructions: 
# Write a function for each arithmetic operation (add, subtract, multiply, divide). 
# If the user entered an invalid operation, print an appropriate message to inform them. 
# Your program handles errors (like dividing by zero) 
# and invalid input (like entering a letter instead of a number).

# Write a function for each arithmetic operation (add, subtract, multiply, divide).
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    else:
        return x / y

# Function to check if input is a valid number
def is_valid_number(value):
    # Allow negative sign at the beginning
    if value.startswith('-'):
        value = value[1:] # exclude '-' sign to validate only the digits

    # Check for more than one decimal point
    if value.count('.') > 1:
        return False

    # Check that all characters are digits or a decimal point
    for char in value:
        if char.isdigit() or char == '.':
            continue # continue to the next character if this check passes
        else:
            return False # return False if the check fails

    return True  # All checks passed
            

# Calculator
def calculator():
    print("Choose an operation: add, subtract, multiply, divide")
    operation = input("Operation: ").strip().lower()

    num1_input = input("Enter first number: ")
    num2_input = input("Enter second number: ")

    # use the is_valid_number function defined above to check whether the input number is valid
    if not is_valid_number(num1_input) or not is_valid_number(num2_input):
        print("Invalid input. Please enter valid numbers.")
        return # an empty return to exit the function

    # convert the input (str) to float to perform arithmetic operations
    num1 = float(num1_input)
    num2 = float(num2_input)

    if operation == "add":
        print("Result:", add(num1, num2))
    elif operation == "subtract":
        print("Result:", subtract(num1, num2))
    elif operation == "multiply":
        print("Result:", multiply(num1, num2))
    elif operation == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation.")

# call the calculator function
calculator()        

print("===================== Exercise 3 =====================")
# Exercise 3

# Create "Guess the Number" game! 
# Your program generates a random number between 1 and 100. 
# Then asks the user to guess the random number. 
# The user have 5 times to guess the number. 
# If they cannot guess it correctly during this 5 rounds, they loose. 
# Each round that the user guess the number wrong, your program gives the user a hint like "Too low!" or "Too high!". 
# If the guess is correct it should print "Correct!" and prints the number of tries.

# Instructions: 
# Write a function to generate a random number. 
# Write a function to ask the user for their guess. 
# Write a function to check if the guess is correct, too high, or too low. 
# Write a main function that loops until the user guesses correctly and provides feedback.
    
# =====================

# Write a function to generate a random number between 1 and 100.
def generate_random_number():
    return random.randint(1, 100)

# Write a function to ask the user for their guess. 
def get_user_guess():
    
    # obtain the user input
    guess_input = input("Guess the number (1-100): ")
   
    # use the is_valid_number function from the previous example to check whether the guess is a valid number
    if not is_valid_number(guess_input):
        print("Invalid input. Please enter a number between 1 and 100.")
        return None
    
    # check whether the number is between 1 and 100
    if int(guess_input) < 1 or int(guess_input) > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        return None
    
    return int(guess_input)

# Write a function to check if the guess is correct, too high, or too low. 
def check_guess(secret, guess):
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"

# Write a main function that loops until the user guesses correctly and provides feedback
def play_game():
    print("--- Exercise 3: Guess the Number ---")
    secret = generate_random_number()
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        guess = get_user_guess()
        if guess is None:
            continue  # Ask again

        result = check_guess(secret, guess)
        print(result)
        
        attempts += 1
        if result == "Correct!":
            print(f"You guessed it in {attempts} tries.")
            return

    print(f"You lost. The number was {secret}.")

# call the play_game function
play_game()
