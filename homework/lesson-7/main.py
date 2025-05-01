# Shopping List
print("\n# Shopping List")
shopping_list = []

shopping = True

while shopping:
    shopping_item = input("Enter an Item ('done' to finish): ")
    if shopping_item.lower() == "done":
         break
    shopping_items.append(shopping_item)
singled_items  = set(shopping_items)
print(singled_items)
shopping_items.sort()
num = 0
for item in singled_items:
    num +=1
    print(f"{num}.{item}")
print(f"Total Number of Items: {len(singled_items)}")
