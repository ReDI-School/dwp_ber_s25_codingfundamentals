# Exercises on Data Structures ( List, Sets Tuples)
print("\n# Exercises on Data Structures ( List, Sets Tuples")

# 1. Exercise 0
print("\n# 1. Exercise 0")

scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
# List
print("\n# list")
print(scores)
# Length(Number of Elements in) of list
print("\n# Length(Number of Elements in) of list")
print(len(scores))

# Exercise 1
print("\n# Exercise 1")

# Count the Number of 3's in the List
print("\n# Count the Number of 3's in the List")
print(scores.count(3))
# Using Counter Method
print("\n# Using Counter Method")
from collections import Counter
print(Counter(scores))

# Exercise 2
print("\n# Exercise 2")
print("Max Score in List", max(scores))

# Exercise 3
print("\n# Exercise 3")

list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm","bar"]
# Common elements
print("\n# Common elements")
for i in list_1:
    for j in list_2:
        if i == j:
            print(i)
# Exercise 4
print("\n# Exercise 4")
all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
# 1. program that goes through every number in the list
print("\n# 1. program that goes through every number in the list")
for a in all_numbers:
    print(all_numbers)
# 2. Append list to a new list called positive_numbers if the number is positive
print("\n# 2. Append list to a new list called positive_numbers if the number is positive")
print("# positive_numbers",)
for a in all_numbers:
    if a > 1:
        print(a)
print("# positive_numbers appended")
positive_numbers = []
for a in all_numbers:
    if a > 1:
        positive_numbers.append(a)
        print(positive_numbers)
# Exercise 5
print("\n# Exercise 5")
# Printing items of the given list in reverse
print("\n# Printing items of the given list in reverse")
reverse_this_list = [10, 20, 30, 40, 50]
reverse_this_list.reverse()
print(reverse_this_list)
# Exercise 6
print("\n# Exercise 6")
# Convert the scores list (from Exercise 0) into a set
print("\n# Convert the scores list (from Exercise 0) into a set")
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
converted_scores_list = set(scores)
print(converted_scores_list)
print(type(converted_scores_list))
# Exercise 7
print("\n# Exercise 7")
# Create a List of Tuples with 5 country names and their capitals, and print the list
print("# Tuples")
country_capital_names = [("Germany","Berlin"),("United Kingdom","London"),("Russia","Moscow"),("France","Paris"),("Greece","Athens")]
print(country_capital_names)
