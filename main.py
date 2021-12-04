from rich.console import Console
from gallow import gallow_frames
from ending import game_over
from the_word import word


c = Console()


def make_gallow(wrong_guesses):
    c.print(gallow_frames[wrong_guesses], style="white")


def enter_word():
    return input("Enter Word: ").upper()


def display_guesses(word, guesses):
    letters = ""
    for letter in word:
        if letter in guesses:
            letters += letter + " "
        elif letter == " ":
            letters += "  "
        else:
            letters += "_ "
    c.print(letters, style="cyan")


def display_wrong_guesses(word, guesses):
    wrong_guesses = ""
    for letter in guesses:
        if letter not in word:
            wrong_guesses += f"{letter} "

    c.print(wrong_guesses, style="magenta")


def get_new_guess(guesses):
    new_guess = input("Make guess: ").upper()
    while new_guess in guesses or new_guess == " ":
        new_guess = input(f"{new_guess} already guessed. Make new guess: ").upper()
    guesses += new_guess[0]
    return guesses


def count_wrong_guesses(word, guesses):
    wrong_guesses = 0
    for letter in guesses:
        if letter not in word:
            wrong_guesses += 1
    return wrong_guesses


def main():
    word_no_dup = "".join(set(word))
    guesses = ""
    wrong_guesses = 0
    playing = True
    while playing:
        make_gallow(wrong_guesses)
        display_guesses(word, guesses)
        display_wrong_guesses(word, guesses)
        guesses = get_new_guess(guesses)
        wrong_guesses = count_wrong_guesses(word,guesses)
        if wrong_guesses >= 6:
            make_gallow(6)
            c.print(game_over, style="red")
            playing = False
        misses = 0
        for letter in word:
            if letter not in guesses and letter != " ":
                misses += 1
        if misses == 0:
            make_gallow(7)
            c.print("Congratulations!\nYou Win!", style="yellow")
            playing = False


if __name__ == '__main__':
    main()