import random

playing = True
carnivores = []
herbivores = []
log = []
animals = [ "Dog", "Cat", "Horse", "Cow", "Pig" ]

def transfer_animal(animal: str, from_pen: list, to_pen: list):
    if animal in from_pen:
        from_pen.remove(animal)
        to_pen.append(animal)
        if from_pen is carnivores:
            from_str = "carnivore pen"
            to_str = "herbivore pen"
        else:
            to_str = "carnivore pen"
            from_str = "herbivore pen"
        action = f"Creature successfully moved from {from_str} to {to_str}"
        print(action)
        log.append(action)
    else:
        print("Creature already in given pen")

def add_animal(animal: str, pen: list):
    pen.append(animal)
    if pen is carnivores:
        to_pen = "carnivore pen"
    else:
        to_pen = "herbivore pen"
    action = f"Added {animal} to {to_pen}"
    log.append(action)
    print(action)

def feed_animal():
    all_animals = carnivores + herbivores
    if len(all_animals) > 0:
        animal = random.choice(all_animals)
        action = f"You fed a {animal}"
        print(action)
        log.append(action)
    else:
        print("No animals found to be fed")

while playing:
    print("Type \"1\" to add animal", "Type \"2\" to feed animal", "Type \"3\" to move animal to between pens", "Type \"9\" to stop playing", sep= '\n')
    do_this = input()
    match do_this:
        case "1":
            a = 1
            for i in animals:
                print(a, i)
                a = a + 1
            animal = animals[int(input("Type number of animal you want to add")) - 1]
            match input("Type \"1\" to add it to carnivore pen or \"2\" for herbivore pen"):
                case "1":
                    add_to_pen_list = carnivores
                case "2":
                    add_to_pen_list = herbivores
            add_animal(animal, add_to_pen_list)
        case "2":
            feed_animal()
        case "3":
            print("Animals:")
            a = 1
            animal_list = carnivores + herbivores
            for i in animal_list:
                print(a, i)
                a = a + 1
            move_this = animal_list[int(input("Type number of animal to move"))-1]
            to_pen = input("To which pen? Type \"1\" for carnivore pen or \"2\" for herbivore pen")
            if to_pen[0] is "1":
                to_pen = carnivores
                from_pen = herbivores
            else:
                to_pen = herbivores
                from_pen = carnivores
            transfer_animal(move_this, from_pen, to_pen)
        case "9":
            playing = False
        
print("\n\nActivity:", log, "\nAnimals:", herbivores, carnivores, sep= '\n')