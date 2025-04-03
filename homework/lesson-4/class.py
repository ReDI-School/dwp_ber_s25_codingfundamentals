# Conditional statements

#price = float(input("price of cokies: "))
#num = int(input("number of cookies: "))
#if num >= 1 and num <= 50:
   # print("cost: = ",price * num)
#elif num >= 50 and num <= 100:
    #print("cost: = ",price * num)
#elif num >= 101:
    #print("cost: = ",price * num)

#DATA Structure
# List

#fruits = []
# fruits = list() empty list

#fruits = ["apple", "banana", "kiwi", "orange"]
#print(fruits)
#append adds element to the end of the list
#fruits.append("pineapple")
#print(fruits) 
#insert element to a specific index
#fruits.insert(2,)

# Exercise 1 List
score_original = [15,19,17,12,17,13]
score = score_original.copy()
print(score[0])
print(score[5])
print(max(score))
print(min(score))
score.append(21)
print(score)
score.sort()
print(score)
score.pop(4)
print(score)
score.remove(17)
print(score)
print(len(score))

#Looping over list
print("\n#Looping over list")

scores =[15,19,17,12,17,13]
for s in scores:
    print(scores)
    print(max(scores))


for s in scores:
    print(s*2)

double_scores = []
for s in scores:
    double_scores.append(s*2)
    print(double_scores)










