# Exercises on Data Structures (Lists, Sets, Tuples)             

## Exercise 0
## Given the following scores, what is the length of the list?
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
print("The length of the scores list is: ", len(scores))

## Exercise 1:
## Given the same list of scores, write a program that counts the number of 3s in the list
## Solution 1
count_of_threes = scores.count(3)
print("The count of 3s - solution 1: ", count_of_threes)

## Solution 2
count_of_3s = 0
for score in scores:
    if score == 3:
        count_of_3s += 1

print("The count of 3s - solution 2: ", count_of_3s)


## Exercise 2:
## Given the same list of scores, find the maximum in the list 
max_score = max(scores)
print("The max score is - solution 1: ", max_score)

max_s = scores[0]  # Assume the first element is the maximum initially
for score in scores:
    if score > max_s: # check whether the current score is greater than previously stored max_s
        max_s = score # update max_s if current score is greater than max_s

print("The max score is - solution 2: ", max_s)


## Exercise 3:
## Given the following two lists, write a program that prints the common elements

list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]

common_elements = []
for item in list_1:
    if item in list_2 and item not in common_elements: # check if item is in list_2 and check if it's already added to the common_elements list
        common_elements.append(item)

print("Common elements - solution 1:", common_elements)

set_1 = set(list_1)
set_2 = set(list_2)
common_set_1 = set_1.intersection(set_2)
print("Common elements - solution 2:", list(common_set_1))


## Exercise 4:
## Given the following list of numbers, write a program
## 1. that goes through each number in the list
## 2. appends it to a new list called `positive_numbers` if the number is positive

all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = []

for num in all_numbers:
  if num > 0:
    positive_numbers.append(num)

print("Positive numbers: ", positive_numbers)

## Exercise 5:
## Print the items of the given list in reverse
reverse_this_list = [10, 20, 30, 40, 50]
reverse_this_list.reverse()
print("Reversed list - solution 1: ", reverse_this_list)

reverse_this_list = [10, 20, 30, 40, 50]
reversed_list_2 = []
for item in reverse_this_list: 
    # insert the number at the first position
    # this keeps replacing the current number at index 0
    reversed_list_2.insert(0, item) 
print("Reversed list - solution 2: ", reversed_list_2)

## Exercise 6
## Convert the scores list (from Exercise 0) into a set and print its elements
scores_set = set(scores)
print("Scores set: ", scores_set)

## Exercise 7
## Create a List of Tuples with 5 country names and their capitals, and print the list
countries_and_capitals = [("Germany", "Berlin"), ("France", "Paris"), ("Austria", "Vienna"), ("Italy", "Rome"), ("Switzerland", "Bern")]
print("Country and capital tuples: ", countries_and_capitals)
