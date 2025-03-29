
# Lesson 3 – Operators, Conditions and Loops

# 1. Basic Arithmetic Operations
print("\n# 1. Basic Arithmetic Operations")
num1 = 5
num2 = 2

print("The first number:", num1)
print("The second number:", num2)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# 2. Modulus and Exponentiation
print("\n# 2. Modulus and Exponentiation")
number = 7

print("The number is:", number)
print("Remainder when divided by 3:", number % 3)
print("Number raised to the power of 2:", number ** 2)

# 3. Odd or Even
print("\n# 3. Odd or Even")
number = 4

print("The number is:", number)
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 4. Compare Two Numbers
print("\n# 4. Compare Two Numbers")
num1 = 10
num2 = 20

print("The first number is:", num1)
print("The second number is:", num2)

if num1 > num2:
    print("The first number is greater than the second.")
elif num2 > num1:
    print("The second number is greater than the first.")
else:
    print("The two numbers are equal.")

# 5. Print Numbers 1 to 10
print("\n# 5. Print Numbers 1 to 10")
for i in range(1, 11):
    print(i)

# 6. Multiplication Table
print("\n# 6. Multiplication Table")
number = int(input("The number is: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 7. FizzBuzz
print("\n# 7. FizzBuzz")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 8. Leap Year
print("\n# 8. Leap Year")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
