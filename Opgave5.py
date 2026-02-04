valid_answers = { "ALT", "STALD", "SALT", "TAL", "DAL", "STAD", "LAD", "SAD" }
letters = {"A", "L", "T", "S", "D"}
correct_answers = []
total_score = 0

def create_word(answer: str):
    if (answer == "EXIT"):
        return -1
    if not (set(answer).issubset(letters)):
        print("Ugyldigt ord, må kun indeholde gyldige bogstaver!")
        return 0
    if (answer in correct_answers):
        print("Du har allerede gættet dette ord!")
        return 0
    elif (answer in valid_answers):
        correct_answers.append(answer)
        print("Godtaget svar!")
        return len(answer)
    else:
        print("Ordet er ikke en gyldig svarmulighed!")
        return 0

while (len(valid_answers) != len(correct_answers)):
    if (len(correct_answers) > 0):
        print("Du har gættet følgende ord så vidt:", correct_answers, f"\nDer mangler at blive gættet {len(valid_answers) - len(correct_answers)} af de angivne muligheder")
    print("Lav et ord ud fra følgende bogstaver eller skriv \"exit for at stoppe\":", letters)
    score = create_word(input().upper())
    if (score < 0):
        break
    else:
        total_score += score
print("Du opnåede en score på:", total_score)
if (len(valid_answers) == len(correct_answers)):
    print("Du gættede alle mulighederne!")