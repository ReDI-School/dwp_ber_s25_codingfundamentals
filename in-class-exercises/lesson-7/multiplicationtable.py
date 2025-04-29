print("expected output")
print("row 1: 1, 2, 3")
print("row 2: 2, 4, 6")
print("row 3: 3, 6, 9")

print("💚 repeating loops")
print("row 1: ", end="")
for column in range(1, 4):
    print(column * 1, end=" | ")
print()
print("row 2: ", end="")
for column in range(1, 4):
    print(column * 2, end=" | ")
print()
print("row 3: ", end="")
for column in range(1, 4):
    print(column * 3, end=" | ")
print()

name = input("What's your name:")
print(f"💖 nested loop for {name}")
size = int(input("table size:")) +1
for column in range(1, size):
    print(f"row {column}: ", end="") # string interpolation 
    for row in range(1, size):
        if column * row <= 9:
            print(column * row, end="  | ")
        else:
            print(column * row, end=" | ")
    print()
