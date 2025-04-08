#Functions
# creat a function that takes two parameters to make a smoothie
def make_smoothie(first_fruit, second_fruit, liquid = "water"):
    print("Here you go, smoothie of " + first_fruit + second_fruit + liquid)
make_smoothie("orange ", "pear ")

# Return
from random import randint
# creat a function that returns a random number between 1 - 100

def generate_a_random_number(start_number, end_number):
    generated_number = randint(start_number, end_number)
    return generated_number
random_number = generate_a_random_number(1, 100)
print("Random number:" + str(random_number))

'''
EXERCISE 1

Write a function `greeting` that takes 2 arguments (first_name and last_name) and prints the following message using the given arguments:
    "Hello, Alice Smith, are you ready for some fun coding today?"
'''

# solution for exercise 1 👇🏽

def greeting(first_name, last_name):
    print("Hello ,", first_name + " "+ last_name + " ," ,"are you ready for some fun coding today?")
greeting("Alice ", "Smith ")


'''
EXERCISE 2

Write a function `repeat_character` that takes a character and a number as arguments and prins a string,
where the character is repeated the specified number of times. 
The number has a default value of 2.
For example, if the character is 'X' and the number is 4, the function should return "XXXX."
'''

# solution for exercise 2 👇🏽
def repeat_character(character, repeat_times = 2):
    print(character * repeat_times)
repeat_character("E", 7)

'''
EXERCISE 3

Copy and paste your solution from exercise 2. 
This time, modify the function so that, if the given number is bigger than 10, it will print out "Sorry, too long!"
'''

# solution for exercise 3 👇🏽
def repeat_character_1(character, repeat_times = 2):
        if repeat_times > 10:
            print("sorry, too long")
        else:
            print(character * repeat_times)
repeat_character_1("x", 11)
repeat_character_1("Z", 4)
repeat_character_1("G")

'''
EXERCISE 4

Create a simple dice roll simulator where you use the randint function to simulate rolling a six-sided die. Follow these steps:
    1. Import the random module to use the randint function.
    2. Create a function that uses randint function to generate a random integer between 1 and 6, and returns the integer.	
    3. Store the function result in a variable
    4. Print out the variable
'''

# solution for exercise 4 👇🏽
from random import randint

# creat a function that returns a random number between 1 - 6

def generate_a_random_number(start_number, end_number):
    generated_number = randint(start_number, end_number)
    return generated_number
random_number = generate_a_random_number(1, 6)
print("Random number:" + str(random_number))
