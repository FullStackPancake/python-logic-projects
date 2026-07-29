import random

my_list = ["popcorn", "microwave", "closet", "chair", "monitor"]
lives = 5
wrong_guesses = []
correct_guesses = []
random_names = random.choice(my_list)

while True:

    display = ""
    for letter in random_names:
        if letter in correct_guesses:
            display += letter
        else :
            display += "_"
    print(display)

    if "_" not in display:
        print("Victory :)")
        break

    guess_letter_on_name = input("Guess a letter on the name: \n")
    if guess_letter_on_name in random_names:
        correct_guesses.append(guess_letter_on_name)
        print("Correct!, let's move to the next letter!")
    elif guess_letter_on_name not in random_names:
        wrong_guesses.append(guess_letter_on_name)
        lives -= 1
        print(f"that's not a valid guess: {lives} left")


    if lives == 0:
        print("Game Over")
        break
    