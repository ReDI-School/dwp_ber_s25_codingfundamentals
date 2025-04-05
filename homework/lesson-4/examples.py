# Calculate the total cost of baking a specific number of cookies (input). The price per cookie decreases as more cookies are baked:
# For 1-50 cookies, the price is 0.50 EUR per cookie.
# For 51-100 cookies, the price is 0.40 EUR per cookie.
# For 101+ cookies, the price is 0.30 EUR per cookie.

print("### Recap Exercise ###\n")

price_1_50 = 0.5
price_51_100 = 0.4
price_101_plus = 0.3

cookies_ordered = int(input("Enter the number of cookies: "))

total_price = 0
if 1 <= cookies_ordered <= 50:
    total_price = cookies_ordered * price_1_50
elif 51 <= cookies_ordered <= 100:
    total_price = cookies_ordered * price_51_100
elif cookies_ordered >= 101:
    total_price = cookies_ordered * price_101_plus

print("Total price for " + str(cookies_ordered) + " cookies is: " + str(total_price) + " EUR")

print("---------------------------------------------------------------------------------")
print("### Lists ###\n")
### Lists

## define an empty list
fruits = list()
fruits = []

## define a list with elements in it
fruits = ["apple", "mango", "banana", "kiwi", "orange"]
print("fruits list: ", fruits)

## access element at a specific index
print("element at index 3: ", fruits[3])

## add a new element to the list 
fruits.append("pear") # adds an element at the end of the list
print("fruits list after appending a new fruit: ", fruits)

## add a new element at a specific index
fruits.insert(2, "strawberry")
print("fruits list after inserting a new fruit at index 2: ", fruits)

## remove an element
fruits.remove("kiwi")
print("fruits list after removing kiwi: ", fruits)

## remove an element at the end of the list
fruits.pop() 
print("fruits list after removing the last fruit: ", fruits)

## remove an element at a specific index
fruits.pop(2)
print("fruits list after removing the fruit at index 2: ", fruits)

## sort the elements in ascending order
## the sort method sorts the elements in-memory, i.e., 
# it changes the position of the elements in the original list and does not return a new list
fruits.sort() 
print("fruits list sorted in ascending order: ", fruits)

## sort the elements in descending order
fruits.sort(reverse=True)
print("fruits list sorted in descending order: ", fruits)

print("---------------------------------------------------------------------------------")
print("### Exercise 1 ###\n")

### Exercise 1
## given this following list of scores:
scores = [15, 19, 17, 12, 17, 13]
print("scores: ", scores)

## print the first score (by accessing it from the list)
print("first score:", scores[0])

## print the last score (by accessing it from the list) 
print("last score - solution 1: ", scores[5])
# or
# using negative index. -1 is the last element, -2 is the second element from last and so on.
print("last score - solution 2:", scores[-1]) 
# or
print("last score - solution 3:", scores[len(scores) - 1]) # len(scores) = 6, and the index goes from 0 to 5

## print the highest score (by accessing it from the list) (Hint: max(example_list))
print("max score: ", max(scores))

## print the lowest score (by accessing it from the list) (Hint: min(example_list))
print("min score: ", min(scores))

## add 21 to the list of scores (Hint: append(number_to_include))
scores.append(21)
print("adding a new score: ", scores)

## sort the scores in increasing order (Hint: sort())
scores.sort()
print("scores list sorted in ascending order: ", scores)

## bonus: remove one of the 17 (Hint: remove(number_to_remove), pop(index))
scores.remove(17)
# or 
index_17 = scores.index(17) # find the index where 17 is stored
scores.pop(index_17) 

print("scores after removing 17: ", scores)

print("---------------------------------------------------------------------------------")
print("### Exercise 2 ###\n")

### Exercise 2
# Exercise 2.1:
# Using the previous scores list, create a new list with double the scores in the first list. 
print("scores: ", scores)
double_scores = []
for score in scores:
    double_scores.append(score*2)
print("doubled scores: ", double_scores)    

# Exercise 2.2:
# Using the previous scores list, try to go through the list with a loop, and find the maximum score.

print("max score - solution 1: ", max(scores))

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score
print("max score - solution 2: ", max_score)

print("---------------------------------------------------------------------------------")
print("### Exercise 3 (Sets) ###\n")
### Exercise 3 (Sets)

## given this following list of scores:
scores = [15, 19, 17, 12, 17, 13]

scores_set = set(scores) # convert a list to a set
print("scores set: ", (scores_set))

## print the first score (by accessing it from the list)
## print the last score (by accessing it from the list) 

# sets are unordered, 
# so it's not possible to access a "first" or a "last" element in a set - as the order can change.
# however, if needed, a set can be converted to a list, 
# and the first and the last elements can be accessed from the list. 


## print the highest score (by accessing it from the list) 
print("max in the set: ", max(scores_set))

## print the lowest score (by accessing it from the list) 
print("min in the set: ", min(scores_set))

## add 21 to the list of scores 
scores_set.add(21)
print("set after adding an element: ", scores_set)

## sort the scores in increasing order
# a set is unordered - so sorting it is not possible
# however, we can convert a set to a list, and then sort it if needed

## bonus: remove one of the 17 
scores_set.remove(17)
print("set after removing an element: ", scores_set)

print("---------------------------------------------------------------------------------")
print("### Exercise 3 (Tuples) ###\n")
### Exercise 3 (Tuples)
## given this following list of scores:
scores = [15, 19, 17, 12, 17, 13]
scores_tuple = tuple(scores)
print("scores tuple: ", scores_tuple)

## print the first score 
print("first score in the tuple: ", scores_tuple[0])

## print the last score (by accessing it from the list) 
print("last score in the tuple: ", scores_tuple[-1])

## print the highest score (by accessing it from the list) (Hint: max(example_list))
print("max score in the tuple: ", max(scores_tuple))

## print the lowest score (by accessing it from the list) (Hint: min(example_list))
print("min score in the tuple: ", min(scores_tuple))

## add 21 to the list of scores (Hint: append(number_to_include))
## sort the scores in increasing order (Hint: sort())
## bonus: remove one of the 17 (Hint: remove(number_to_remove), pop(index))

# tuples are unchangeable - so, it's not possible to add/remove elements
