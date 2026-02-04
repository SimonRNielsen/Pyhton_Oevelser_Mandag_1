replies = { "Ja": True, "Nej": False, "Næh": False, "Absolut ikke": False}
quiz = { "Er dette en quiz?": replies, "Er det en træls opgave?": replies, "Skal den bare hurtig overstås?": replies }
correct = 0
wrong = 0

def ask_question(question):
    print(f"{question} - svarmuligheder: {list(quiz[question].keys())}")
    answer = ""
    while answer not in quiz[question]:
        answer = input("Angiv et gyldigt svar:\n").capitalize()
    return quiz[question][answer]

for question in quiz:
    if (ask_question(question)):
        print("Korrekt svar!")
        correct += 1
    else:
        print("Forkert svar!")
        wrong += 1
print(f"Du havde {correct} rigtig(e) og {wrong} forkert(e) svar!")