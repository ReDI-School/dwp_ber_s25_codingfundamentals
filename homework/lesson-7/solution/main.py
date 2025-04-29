shopping_list = []

while True:
    item = input("Enter an item ('done' to finish): ").strip()
    if item.lower() == 'done':
        print("\nYour shopping list:")
        if not shopping_list:
            print("Empty list")
        else:
            sorted_list = sorted(shopping_list) # BONUS: sorting list with sorted()
            for index, item in enumerate(sorted_list, start=1):
                print(f"{index}. {item}")
            print("\nTotal items:", len(sorted_list))
        break
    if item == "":
        continue
    if item in shopping_list:
        print("Duplicate item. Not added.") # BONUS: duplicated item handling
    else:
        shopping_list.append(item)