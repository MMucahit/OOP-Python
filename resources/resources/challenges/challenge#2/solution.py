from string import ascii_letters, punctuation
from random import choices
from copy import copy


class Password:
    """A password of customize strength and length.

    Encapsulate a randomly generate password depending on the user-specified strength and length, where the latter
    is optional and automatically set depending on the strength (low -> 8, mid -> 12, high -> 16). If a length is
    user-specified these presets are overridden regardless of the strength.

    :param strength: a measure of the password's effectiveness against brute-force guessing
    :type strength: str, optional

    :param length: the length of the password
    :type length: int, optional
    """

    INPUT_UNVIERSE = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation)
    }

    DEFAULT_LENGTHS = {
        "low": 8,
        "mid": 12,
        "high": 16
    }

    @classmethod
    def show_input_universe(cls):
        """Return the complete input universe from which characters are sampled

        :return: The universe of characters from which random sampling is done to generate passwords
        :rtype: dict (of list-s)
        """
        return cls.INPUT_UNVIERSE

    def __init__(self, strength="mid", length=None):
        """Constructor method"""
        self.strength = strength
        self.length = length

        self._generate()

    def _generate(self):
        """Generates the password according to the strength and length specified at initialization

        :return: the randomly generated password
        :rtype: str
        """

        population = copy(self.INPUT_UNVIERSE["letters"])
        length = self.length or self.DEFAULT_LENGTHS.get(self.strength)

        if self.strength == "high":
            population += self.INPUT_UNVIERSE["numbers"] + self.INPUT_UNVIERSE["punctuation"]
        else:
            population += self.INPUT_UNVIERSE["numbers"]

        self.password = "".join(list(map(str, choices(population, k=length))))


if __name__ == "__main__":
    p_weak = Password(strength="low")
    print("Weak password: " + p_weak.password)

    p_mid = Password(strength="mid", length=40)
    print("Mid password: " + p_mid.password)

    p_high = Password(strength="high")
    print("High password: " + p_high.password)

    p_default = Password()
    print("Default password: " + p_default.password)
