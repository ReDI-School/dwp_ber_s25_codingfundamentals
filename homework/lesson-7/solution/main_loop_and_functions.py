"""
this is a bit more advanced solution combining contents from lesson 6 and 7, 
Lesson 6: functions and Lesson 7: loops
notice the definition of the function contains new things: 

def add_item(item: str, shopping_list: list)
str and list in this case indicates which datatype should be passed to the function
items should be an string, and shopping_list should be a list.

-> list, 
this means that the function returns a list, 
-> None, 
this means that the function doesn't have a return, for example display_list()
only prints values but doesn't return anything

main(shopping_list = [])
shopping_list = [] means that if main is called without an argument, 
then the variable shopping_list defaults to and empty list []

is not required to write this elements, but you are going to see this notatition a lot
mostly when reading documentation, so is good to get used to it.
"""

def add_item(item: str, shopping_list: list) -> list:
    if item in shopping_list:
        print("Duplicate item. Not added.") 
        return shopping_list # BONUS: duplicated item handling
    shopping_list.append(item)
    return shopping_list

def display_list(shopping_list: list) -> None:
    if not shopping_list:
        print("Empty list")
        return
    print("\nYour shopping list:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    print("\nTotal items:", len(shopping_list))

def main(shopping_list = []) -> None:
    while True:
        item = input("Enter an item ('done' to finish): ").strip()
        if item.lower() == 'done':
            sorted_list = sorted(shopping_list) # BONUS: sorting list with sorted()
            display_list(sorted_list)
            break
        if item == "":
            continue
        shopping_list = add_item(item, shopping_list)

main()