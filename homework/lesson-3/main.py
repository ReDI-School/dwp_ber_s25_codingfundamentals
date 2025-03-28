# Basic Arithmetic Operations
a = int(input("enter first number "))
b = int(input("enter second number "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 2. Modulus and Exponentiation
number = int(input("enter number "))
print(number % 3)
print(number ** 2)

# 3.Odd and Even
count = int(input("enter number "))
if count % 2 == 0:
    print(count)
elif count % 2 != 0:
    print("Odd Number")

# 4. Compare Two Numbers
first_number = int(input("enter number1 "))
second_number = int(input("enter number2 "))
if first_number > second_number:
    print("The first number is greater than the second number")
elif second_number > first_number:
    print("The second number is greater than the first number")
else:
    print("The two numbers are equal")

# 5. Print Numbers 1 to 10
for count1 in range (1, 11):
    print(count1)

# self thought 1

for days in range (int(input("enter number "))):
    print(days)

# self thought 2

months = int(input("enter number "))
for months in range(1, 11):
    print(months)

# 6. Miltiplication Table

num = int(input("enter number "))
for n in range(1, 11):
    print(num,"*",n,"=", num * n)

# 7. FizzBuzz
for zahl in range(1, 21):
    if zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")
    elif zahl % 3 ==0:
        print("Fizz")
    elif zahl % 5 == 0:
        print("Buzz")
    else:
        print(zahl)
    
# 8. Leap year

year = int(input("enter year"))
if year % 100 == 0 and year % 400 != 0:
    print("Not Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
elif year % 400 == 0:
    print("Leap Year")





    

