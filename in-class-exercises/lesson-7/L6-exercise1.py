from random import randint

rand_numbers=[]
# non_duplicated = set(rand_numbers)

def generation_numbers ():
    count=0
    while count < 10:
        number = randint(0, 100)
        if number not in rand_numbers:
            rand_numbers.append(number)
        count+=1
    return rand_numbers

rand_numbers1 = generation_numbers()
print(rand_numbers1)

sum = sum(rand_numbers1)
len = len(rand_numbers1)

from statistics import mean
import numpy as np

average1 = sum / len
average2 = mean(rand_numbers1)
average3 = np.mean(rand_numbers1)
print ("The average1 ", average1)
print ("The average2 ", average2)