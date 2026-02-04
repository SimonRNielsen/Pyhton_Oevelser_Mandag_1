question_one = { "Ja": True, "Nej": False, "Næh": False, "Absolut ikke": False}
question_two = { "Ja": True, "Nej": False, "Næh": False, "Absolut ikke": False}
question_three = { "Ja": True, "Nej": False, "Næh": False, "Absolut ikke": False}
questions = { "Er dette en quiz?": question_one, "Er det en træls opgave?": question_two, "Skal den bare hurtig overstås?": question_three }
correct = 0
wrong = 0

def ask_question(question):
    answers = questions[question]
    print(f"{question} - svarmuligheder: {list(answers.keys())}")
    answer = input("Vælg et svar:\n")
    if (questions[question][answer] is True):
        return True
    else:
        return False

for i in questions:
    if (ask_question(i) is True):
        print("Korrekt svar!")
        correct += 1
    else:
        print("Forkert svar!")
        wrong += 1
print(f"Du havde {correct} rigtig(e) og {wrong} forkert(e) svar!")