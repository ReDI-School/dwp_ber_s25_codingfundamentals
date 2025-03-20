# 1.Variables and Basic data types
my_number = 10
my_string = "Hello, Python!"
my_float = 3.14
print(my_number)
print(my_string)
print(my_float)

# 2. Working with different data types
# a. String Concatenation
first_name = "Bella "
last_name = "Heinz"
full_name = (first_name + last_name)
print(full_name)

# b. Arithmatic Operations
a = 5
b = 3
add_results = (a + b)
sub_results = (a - b)
mult_result = (a * b)
div_result = (a / b)
print(add_results)
print(sub_results)
print(mult_result)
print(div_result)

# 3. Booleans and Comparisons
# a. Creating Booleans
is_greater = 5>3
is_equal = 5==3
is_smaller = 5<3
print(is_greater)
print(is_equal)
print(is_smaller)
# b. Boolean Operations
booi1 = True
booi2 = False
# AND
print(booi1 and booi2)
print(True and False)
# OR
print(booi1 or booi2)
print(True or False)
# NOT
print(not booi1)
print(not False)
print(not booi2)
print(not False)

# c. Comparison between Data types
pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"
# 1.
print(pi == pi_pi)
print(type(pi))
print(type(pi_pi))

# 2.
print(pi_pi == pi_pi_pi)

# 4. Type checking and conversion
# a. Type checking 

print(type(pi))
print(type(pi_pi))
print(type(pi_pi_pi))

# b. Type conversion

my_str = "123"
my_int = int(my_str)
my_float_converted = float(my_int)
print(my_str)
print(my_int)
print(my_float_converted)

# 5. Challenge
celsius = 50
fahrenheit = ((celsius * 9/5) + 32)
print(celsius)
print(fahrenheit)





















