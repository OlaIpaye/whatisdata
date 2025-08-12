# Toy box = Dataset
toy_box = [
    {"name": "Teddy Bear", "type": "Stuffed Animal", "color": "Brown"},
    {"name": "Race Car", "type": "Vehicle", "color": "Red"},
    {"name": "Lego Set", "type": "Blocks", "color": "Multi"},
    {"name": "Action Figure", "type": "Doll", "color": "Blue"},
    {"name": "Teddy Bear", "type": "Stuffed Animal", "color": "Brown"}  # duplicate row
]

# Print all toys = all row of data
print("Here's what's in my toy box")
for toy in toy_box:
    print(f"{toy["name"]}, {toy["type"]}, {toy["color"]}")

print("\nNumber of toys:", len(toy_box))