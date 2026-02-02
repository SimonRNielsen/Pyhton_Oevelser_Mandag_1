from array import array
import random

guesses = array('i', [])

def validate_input(input: str):
    if input.isdigit() and int(input) not in guesses:
        return True
    else:
        return False

guesses_remaining = 7
secret_number = random.randint(1, 100)

while (guesses_remaining > 0):
    guess = input(f"Gæt et tal mellem 1-100, du har {guesses_remaining} gæt, eller skriv et tal udover grænserne for at afslutte\n")
    if validate_input(guess):
        guess = int(guess)
        if guess <= 0 or guess > 100:
            guesses_remaining = 0
        elif guess == secret_number:
            print("Rigtigt gæt! Tak fordi du spillede med...")
            guesses_remaining = 0
        elif guess < secret_number:
            print("Det hemmelige tal er højere end dit gæt")
            guesses.append(guess)
            guesses_remaining -= 1
        else:
            print("Det hemmelige tal er lavere end dit gæt")
            guesses.append(guess)
            guesses_remaining -= 1
        if guesses_remaining == 0:
            print(f"Du har tabt, du gættede ikke det hemmelige tal, det hemmelige tal var {secret_number}")
        print("Tidligere gæt:", guesses, sep='\n')
    else:
        print("Gættet må ikke indeholde bogstaver eller tidligere gæt!")