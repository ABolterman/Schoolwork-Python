from Words import word_list
import random
# https://stackoverflow.com/questions/14573021/python-using-variables-from-another-file

# write a function: get_random_word() that returns a random word from the word list
def get_random_word():
    return random.choice(word_list)


# write a function: display_hidden_word( hidden_word, letters_guessed )
# - prints on 1 line, a blank if you haven't guessed the letter, or the letter if you have guessed it
def display_hidden_word(hidden_word, letters_guessed):
    output = ""
    for letter in hidden_word:
        if letter in letters_guessed:
            output += letter
        else:
            output += "_"
    print(output)


# write a function: get_letter_guess( letters_guessed )
# - don't allow the user to guess a letter they have already guessed
# - also ensure the guess is only a single letter
# - returns the letter guessed
def get_letter_guess(letters_guessed):
    for i in range(0, 100000000):
        letter = input("Type a letter, or \"guesses\" to see guessed letters. \n")
        if letter == "guesses":
            letters_guessed.sort()
            guessed_string = ", ".join(letters_guessed)
            print(guessed_string)
            continue
        if letter in letters_guessed:
            print("You already guessed that letter!")
            continue
        if len(letter) != 1:
            print("That's more than 1 letter")
            continue
        else:
            break
    return letter


# write a function: has_the_word_been_guessed( hidden_word, letters_guessed )
# - return true if the word has been guessed
def has_the_word_been_guessed(hidden_word, letters_guessed):
    output = ""
    for letter in hidden_word:
        if letter in letters_guessed:
            output += letter
        else:
            output += "_"
    if "_" in output:
        return False
    else:
        return True


# write a function print_gallows( number_of_incorrect_guesses )
# - prints the gallows with the correct number of body parts
def print_gallows(number_of_incorrect_guesses):
    # Bars taken from https://coolsymbol.com/
    gallows_list = ["", " ╔════╗", " ║    ", " ║  ", " ║   ", "═╩═"]
    # Emojis taken from https://getemoji.com/
    if number_of_incorrect_guesses >= 1:
        gallows_list[2] = " ║   😧"
    if number_of_incorrect_guesses >= 2:
        gallows_list[3] = " ║   👕"
    if number_of_incorrect_guesses >= 3:
        gallows_list[3] = " ║ 💪👕"
    if number_of_incorrect_guesses >= 4:
        gallows_list[3] = " ║ 💪👕🤳"
    if number_of_incorrect_guesses >= 5:
        gallows_list[4] = " ║   🦵"
    if number_of_incorrect_guesses >= 6:
        gallows_list[4] = " ║  🦵🦵"
    for i in range(0, len(gallows_list)):
        print(gallows_list[i])


# write a function has_person_been_hanged( number_of_incorrect_guesses )
# - returns true or false
def has_person_been_hanged(number_of_incorrect_guesses):
    if number_of_incorrect_guesses == 6:
        return True
    else:
        return False


incorrect_guess_number = 0
play = ""
list_of_guessed_letters = []
secret_word = get_random_word()
while play != "n":
    play = ""
    guessed_letter = get_letter_guess(list_of_guessed_letters)
    list_of_guessed_letters.append(guessed_letter)
    display_hidden_word(secret_word, list_of_guessed_letters)
    if guessed_letter not in secret_word:
        incorrect_guess_number += 1
        print_gallows(incorrect_guess_number)
    if has_the_word_been_guessed(secret_word, list_of_guessed_letters):
        print("Congrats! You Won!")
        play = input("Play again? y/n")
    if has_person_been_hanged(incorrect_guess_number):
        print("Too bad! You lost!")
        print(f"The word was \"{secret_word}\".")
        play = input("Play again? y/n")
    if play == "y":
        secret_word = get_random_word()
        list_of_guessed_letters = []
        incorrect_guess_number = 0
