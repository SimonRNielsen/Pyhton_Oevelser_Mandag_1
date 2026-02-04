valid_answers = { "ALT", "STALD", "SALT", "TAL", "DAL", "STAD", "LAD", "SAD" }
letters = {"A", "L", "T", "S", "D"}
correct_answers = []
playing = True
total_score = 0

def create_word(answer: str):
    if (answer == "EXIT"):
        return -1
    if not (set(answer).issubset(letters)):
        print("Ugyldigt ord, må kun indeholde gyldige bogstaver!")
        return 0
    if (correct_answers.__contains__(answer)):
        print("Du har allerede gættet dette ord")
        return 0
    elif (valid_answers.__contains__(answer)):
        correct_answers.append(answer)
        return answer.__len__()
    else:
        print("Ordet er ikke en gyldig svarmulighed")
        return 0

while (len(valid_answers) != len(correct_answers) and playing):
    if (len(correct_answers) > 0):
        print("Du har gættet følgende ord så vidt:", correct_answers)
    print("Lav et ord ud fra følgende bogstaver eller skriv \"exit for at stoppe\":", letters)
    score = create_word(input().upper())
    if (score < 0):
        playing = False
    else:
        total_score += score
print(f"Du opnåede en score på: {total_score}")
if (len(valid_answers) == len(correct_answers)):
    print("Du gættede alle mulighederne!")