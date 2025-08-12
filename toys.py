# Toy box = Dataset
toy_box = [
    {"name": "Teddy Bear", "type": "Stuffed Animal", "color": "Brown"},
    {"name": "Race Car", "type": "Vehicle", "color": "Red"},
    {"name": "Lego Set", "type": "Blocks", "color": "Multi"},
    {"name": "Action Figure", "type": "Doll", "color": "Blue"},
    {"name": "Teddy Bear", "type": "Stuffed Animal", "color": "Brown"},  # duplicate row
]

# Adds 2 more toys to the toy box
new_toys = [{"name": "Puzzles", "type": "Creative", "color": "Multi"},
    {"name": "Toy Soldier", "type": "Action Figures", "color": "Black"}]

toy_box.extend(new_toys)

# Prints all toys = all row of data
print("Here's what's in my toy box")
for toy in toy_box:
    print(f'{toy["name"]}, {toy["type"]}, {toy["color"]}')

# Prints out number of toys in the box
print("\nNumber of toys:", len(toy_box))

