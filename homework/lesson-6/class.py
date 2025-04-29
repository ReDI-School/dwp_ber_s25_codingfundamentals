''' # Exercise 1:
- Write an if statement which checks if a value is above a given quota. If the
value is greater or equal to the quota, print "Done". Otherwise print "Not
done"'''
# Exercise 1:
print("\n# Exercise 1:")
age = int(input("Type your age: "))
if age >= 35:
    print("Done")
else:
    print("Not done")

'''# Exercise 2:
- Copy/paste your code above and slightly tweak it to change what is being
printed:
- If the value is greater or equal to the quota, print 0 (zero)
- Otherwise print the result of: quota - value  '''
# Exercise 2
print("\n# Exercise 2")

quota = 35
age = int(input("Type your age: "))
if age >= 35:
    print(0)
else:
    print("quota- age:",quota - age)


''' # Exercise 3:
 - Create/define a function called 'fruits_remaining' which takes two
parameters: 'fruits_picked' and 'fruits_quota' and return the remainder of
fruits to pick:
- 0 if the fruits_picked is greater or equal to the fruits_quota, otherwise
fruits_quota - fruits_picked.'''

# Exercise 3:
print("\n# Exercise 3:")

def fruits_remaining(fruits_quota, fruits_picked):
    
    fruits_quota = int(input("Type fruitsquota: "))

    fruits_picked = int(input("Type fruits picked:"))
    
    if fruits_picked >= fruits_quota:
        print(0)
    else:
        print("rest:",fruits_quota - fruits_picked)
    
fruits_remaining("fruits_quota", "fruits_picked")

'''# Exercise 4:
- Call your function with a few different combination of values, and then print
the result returned by your function.'''

# Exercise 4: Calling the Function
print("\n# Exercise 4: Calling the Function")

fruits_remaining("fruits_quota","fruits_picked")

'''# Bonus Exercise: 
# Exercise Bonus:
- Let's say a fruit picker picks an amount of fruits 4 days a week.
- If they reach quota, they get Friday free, otherwise they have to work on Friday.
- Create/define a function called is_friday_off which takes parameters, a list of
'fruit_picks' and 'fruits_quota'. This function should return a boolean value:
- True if the fruit picker has reached quota and gets Friday off.
- False if the fruit picker has not reached quota and does not get Friday off.

- Call this function with the two following lists, and a quota of 880.
fruit_picks_1 = [223, 212, 202, 234]
fruit_picks_2 = [200, 256, 189, 240]'''
# Bonus Exercise:
print("\n# Bonus Exercise ")

def is_friday_off(fruits_quota1, f_pick): 


    if f_pick >= fruits_quota1:
        gets_friday_off = True
        print("gets friday off: ", gets_friday_off)
    else:
        does_not_get_friday_off = False
        print("does not get friday off: ", does_not_get_friday_off)

is_friday_off(50,sum([22,44,3]))
is_friday_off(880, sum([223,212,202,234]))
is_friday_off(880, sum([200,256,189,240]))



    
    
    





