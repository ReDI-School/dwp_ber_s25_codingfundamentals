from random import randint

# unpacking range into list
numbers = [*range(1,6)] 
# equivalent to range(1,6) but done manually:
numbers = [1, 2, 3, 4, 5]
#indexes - 0  1  2  3  4
print(numbers)

# printing hello 5 times
for i in range(1,6):
    print(numbers[randint(0,4)], "hello")

# printing a list
fruits = ["banana", "mango", "apple"]
print("✅ begining the loop")
for fruit in fruits:
    print("🍇",fruit)
print("💚 loop finished")

# operating over a list
print("🔢 doubling numbers")
numbers = [1, 2, 3, 4, 5]
doubled = []
for number in numbers:
    doubled.append(number * 2)
print("doubled numbers:", doubled)

