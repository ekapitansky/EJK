import random

random_number = random.randint(1, 10)
tries = 0
tries_remaining = 3
has_won = False


def test_number(guess_num, tries, tries_remaining, has_won):
    if not guess_num > 0 or not guess_num < 11:
        print("That number is not between 1 and 10.")
        tries -= 1
        tries_remaining += 1

    elif guess_num == random_number:
        print("Congratulations! You are correct!")
        print("It took you" (tries), "tries.")
        has_won = True

    elif guess_num == random_number+1 or-1:
        if tries_remaining > 0:
            print("Hot. You have" (tries_remaining), "tries remaining.")
        else:
            print("Sorry, but my number was "(random_number), ".")
            print("You are out of tries. Better luck next time.")

    elif guess_num == random_number+2 or-2:
        if tries_remaining > 0:
            print("Warm. You have ", (tries_remaining), "tries remaining.")
        else:
            print("Sorry, but my number was "(random_number), ".")
            print("You are out of tries. Better luck next time.")


    return (tries, tries_remaining, has_won)


def main(random_number, tries, tries_remaining, has_won):
    while tries < 3:
        guess = input("Guess a random number between 1 and 10. ")
        tries += 1
        tries_remaining -= 1

        try:
            guess_num = int(guess)
            tries, tries_remaining, has_won = test_number(guess_num, tries, tries_remaining, has_won)

        except:
            print("That's not a whole number!")
            tries -= 1
            tries_remaining += 1



main(random_number, tries, tries_remaining, has_won)