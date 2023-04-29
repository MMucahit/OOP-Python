from string import ascii_letters, punctuation
from random import choices
from copy import copy

class Password:
    INPUT_UNIVERSE = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation)
    }

    DEFAULT_LENGTH = {
        "low": 8,
        "mid": 12,
        "high": 16
    }

    @classmethod
    def show_input_universe(cls):
        return cls.INPUT_UNIVERSE
    
    def __init__(self, strength, length=None):
        self.strength = strength
        self.length = length

        self._generate()

    def _generate(self):
        ### Mutable object issue, we have to carefull that use mutable object for class instance
        ## If we didn't use copy, 
        # population point list of letters[INPUT_UNIVERSE] object reference 
        # when population has changed list of letters will be affected that.
        population = copy(self.INPUT_UNIVERSE["letters"])
        length = self.length or self.DEFAULT_LENGTH[self.strength]

        if self.strength == "high":
            population += self.INPUT_UNIVERSE['numbers'] + self.INPUT_UNIVERSE['punctuation']
        
        else:
            population += self.INPUT_UNIVERSE['numbers']

        self.password = "".join(list(map(str, choices(population, k=length))))

if __name__ == "__main__":
    p_weak = Password(strength='low')
    print(f"Weak password: {p_weak.password} - {p_weak}")

    p_mid = Password(strength='mid')
    print(f"Mid password: {p_mid.password} - {p_mid}")

    p_high = Password(strength='high')
    print(f"High password: {p_high.password} - {p_high}")

    p_default = Password(strength='mid')
    print(f"Default password: {p_default.password} - {p_default}")