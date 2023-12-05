
def organize_inventory(beverage_inventory):
    sorted_inventory = sorted(beverage_inventory, key=lambda x: x['name'])

    return sorted_inventory
inventory = [
    {'name': 'Water', 'type': 'Non-alcoholic', 'quantity': 100},
    {'name': 'Cola', 'type': 'Soda', 'quantity': 50},
    {'name': 'Orange Juice', 'type': 'Juice', 'quantity': 75},
    {'name': 'Coffee', 'type': 'Hot beverage', 'quantity': 30},
]

organized_inventory = organize_inventory(inventory)
for beverage in organized_inventory:
    print(beverage)
