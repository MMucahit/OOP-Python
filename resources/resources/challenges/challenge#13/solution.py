#
#
#
import time
from collections import defaultdict
from string import ascii_lowercase
from random import choice


class LetterGuessingException(Exception):
    """The exception base class for the Letter Guessing App"""


class LetterComesAfter(LetterGuessingException):
    pass


class LetterComesBefore(LetterGuessingException):
    pass


class NotALetter(LetterGuessingException):
    pass


class LetterGuessingGame:
    def __init__(self):
        self.start_time = time.time()
        self.performance = defaultdict(list)
        self._correct_guess = False

    def _display_performance(self):
        time_taken = time.time() - self.start_time
        return f"{'That was correct!' if self._correct_guess else 'Game interrupted.'} You played for {round(time_taken, 2)} seconds, and made " \
               f"{len(self.performance['before'])} before guesses and " \
               f"{len(self.performance['after'])} after guesses"

    @staticmethod
    def _pick_a_letter():
        print("The computer has chosen a letter from the English alphabet... what do you think it was?")
        return choice(list(ascii_lowercase))

    @staticmethod
    def _validate_user_input(computer_choice, user_guess):
        if user_guess not in ascii_lowercase:
            raise NotALetter
        elif user_guess < computer_choice:
            raise LetterComesAfter
        elif user_guess > computer_choice:
            raise LetterComesBefore

    def play(self):
        computer_choice = self._pick_a_letter()
        user_guess = None

        while True:
            try:
                user_guess = input().strip().lower()
                self._validate_user_input(computer_choice, user_guess)

                self._correct_guess = True
                break
            except LetterComesAfter:
                print("Nope, it was something after, guess again\n")
                self.performance["before"].append(user_guess)
            except LetterComesBefore:
                print("Nope, it was something before, guess again\n")
                self.performance["after"].append(user_guess)
            except NotALetter:
                print("Only English alphabet letters are supported\n")
            except KeyboardInterrupt:
                print(self._display_performance())

        print(self._display_performance())


if __name__ == "__main__":
    game = LetterGuessingGame()
    game.play()
