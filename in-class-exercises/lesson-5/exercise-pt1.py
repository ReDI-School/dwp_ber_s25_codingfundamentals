'''
EXERCISE 1

Write a function `greeting` that takes 2 arguments (first_name and last_name) and prints the following message using the given arguments:
    "Hello, Alice Smith, are you ready for some fun coding today?"
'''

# solution for exercise 1 👇🏽

def greeting(first_name, last_name):
  print("Hello, " + first_name + " " + last_name + " are you ready for some fun coding today!")


'''
EXERCISE 2

Write a function `repeat_character` that takes a character and a number as arguments and prins a string,
where the character is repeated the specified number of times. 
The number has a default value of 2.
For example, if the character is 'X' and the number is 4, the function should return "XXXX."
'''

# solution for exercise 2 👇🏽


def repeat_character(character, number=2):
  print(character * number)

  # Alternatively, you can also use for loop to solve this
  '''
  result = ""
  for _ in range(number):
    result += character
    print(result)
  '''

'''
EXERCISE 3

Copy and paste your solution from exercise 2. 
This time, modify the function so that, if the given number is bigger than 10, it will print out "Sorry, too long!"
'''

# solution for exercise 3 👇🏽


def repeat_character_2(character, number=2):
  if number > 10:
    print("Sorry, too long")
  else:
    print(character * number)
