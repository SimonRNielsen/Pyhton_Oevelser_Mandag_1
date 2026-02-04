replies = { "Ja": True, "Nej": False, "Næh": False, "Absolut ikke": False}
questions = { "Er dette en quiz?": replies, "Er det en træls opgave?": replies, "Skal den bare hurtig overstås?": replies }
correct = 0
wrong = 0

def ask_question(question):
    answers = questions[question]
    print(f"{question} - svarmuligheder: {list(answers.keys())}")
    answer = input("Vælg et svar:\n").capitalize()
    return questions[question][answer]

for i in questions:
    if (ask_question(i)):
        print("Korrekt svar!")
        correct += 1
    else:
        print("Forkert svar!")
        wrong += 1
print(f"Du havde {correct} rigtig(e) og {wrong} forkert(e) svar!")