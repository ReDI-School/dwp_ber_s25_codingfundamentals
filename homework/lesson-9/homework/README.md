# Python Exercises

from inquire import inquire
import random


## Exercise 1: Student Grouping
Imagine you are a teacher who needs to group their students into pairs or small groups. Given the following list of dictionaries, create random pairs or groups of students – each pair has to have the same project choice.

```python
students = [
    {
        "name": "Jane",
        "choice": "Project B"
    },
    {
        "name": "Janet",
        "choice": "Project A"
    },
    {
        "name": "Jack",
        "choice": "Project A"
    },
    {
        "name": "Jimmy",
        "choice": "Project B"
    },
    {
        "name": "Jean",
        "choice": "Project A"
    },
    {
        "name": "Juan",
        "choice": "Project B"
    },
    {
        "name": "Juanita",
        "choice": "Project B"
    },
    {
        "name": "Janine",
        "choice": "Project A"
    },
    {
        "name": "Jill",
        "choice": "Project B"
    },
    {
        "name": "John",
        "choice": "Project B"
    },
]
```

Example pairs:
- Pair 1: [John, Jane] (they both have Project B)
- Pair 2: [Janine, Janet] (they both have Project A)

You can use the following helper function:
```python
def pick_random_name(list_names):
    random_name = random.choice(list_names)
    return random_name
```

**Bonus**: Make your code into a function which returns the list of pairs.

## Exercise 2: Meal cost calculator
### Preparation
Run the following code a few times to understand what is happening. The 'inquire' function will ask 3 questions for each person. You don't need to understand how the 'inquire' function works, you just need to use it. You will be able to select one of two options for each question asked. You will then need to do some calculations based on the result created by the 'inquire' function.

```python
import inquirer
import random

def inquire(name):
  breakfast_base = random.randint(2, 6)
  lunch_base = random.randint(10, 21)
  dinner_base = random.randint(30, 51)
  questions = [
      inquirer.List(
          "breakfast",
          message=f"How much did {name} pay for breakfast? 🥐 ☕",
          choices=[f"${breakfast_base}", f"${breakfast_base + 2}"],
      ),
      inquirer.List(
          "lunch",
          message=f"How much did {name} pay for lunch? 🍔",
          choices=[f"${lunch_base}", f"${lunch_base + 7}"],
      ),
        inquirer.List(
          "dinner",
          message=f"How much did {name} pay for dinner? 🍽️",
          choices=[f"${dinner_base}", f"${dinner_base + 15}"],
      ),
  ]
  
  transactions = inquirer.prompt(questions)
  return {name: transactions}

people = ["John", "Jane", "Janet"]
result = [inquire(person) for person in people]
print("Result: ")
pprint(result)
```

Write a function which calculates the sum of the 3 meals for each friend (use the 'result' variable as input to your function).

Example output:
- Jane sum: $74

The `convert_dollars` function will help you convert the strings given in our result list into numbers that you can use to perform calculations. From $X (type str) to X (type int)

```python
def convert_dollars(value):
    number_value = int(value.replace("$", ""))
    return number_value
```
**Bonus**: - Replace the value of the name variable with your own name.

## Exercise 4: Meal cost game
Run this code a few times and try to understand how the game works to then be 
able to try and win the game. Slightly change the low and high limit range to make the game easier to win.

```python
def play_game():
    name = "ReDi"
    lower_limit = 42 
    higher_limit = 55 
    meals = inquire(name)[name] 
    total = 0

    for meal_value in meals.values(): 
        total += convert_dollars(meal_value) 
    if (lower_limit > total or higher_limit < total): 
        print("You lost.. try again!") 
    else: 
        print("Congrats! You won 👏")

# Uncomment the lines below to test your answer 👇👇👇
# play_game()
```

## Exercise 4: Credit Card Masking
Complete the `mask_credit_card_number` function that takes in a 16-digit credit card number and masks all but the last 4 digits.

```python
sample_credit_card_number = '1234567890987654'
expected_credit_card_result = 'XXXXXXXXXXXX7654'

def mask_credit_card_number(credit_card_number):
    masked_credit_card_number = ''
    # write your code here!
    return masked_credit_card_number

# Uncomment the lines below to test your answer 👇👇👇
# print('Expected result: ', expected_credit_card_result)
# result = mask_credit_card_number(sample_credit_card_number)
# print('Your result:', result)
```
