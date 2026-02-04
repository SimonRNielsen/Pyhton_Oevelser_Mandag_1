import random

consumables, monsters, gear = [], [], []
unsorted_list = [('Bread', 'Consumable'), ('Mystery Meat', 'Consumable'), ('Dragon', 'Monster'), ('Beholder', 'Monster'), ('Sword', 'Gear'), ('Armor', 'Gear')]

def sort_item(selected: str):
    if unsorted_list[random_selection][1].lower() == selected.lower():
        match selected.lower():
            case "consumable":
                consumables.append(unsorted_list[random_selection])
            case "monster":
                monsters.append(unsorted_list[random_selection])
            case "gear":
                gear.append(unsorted_list[random_selection])
        unsorted_list.remove(unsorted_list[random_selection])
        print("Correctly sorted!")
    else:
        print("Wrong sorting, you're a bad wizard!")

while len(unsorted_list) > 0:
    random_selection = random.randint(0, len(unsorted_list) - 1)
    print(f"Sort the following item into the correct list (Consumable, Monster or Gear): {unsorted_list[random_selection][0]}")
    sort_item(input())
print("Congratulations, you correctly sorted all objects")
print(consumables, monsters, gear, sep='\n')