#
#
#
from random import choices
import re


class MasterCardMixin:
    def generate(self):
        return [5, 3] + super().generate()


class VisaMixin:
    def generate(self):
        return [4, 2] + super().generate()


class ValidMixin:
    def generate(self):
        number = super().generate()
        return number[:-1] + [self.calculate_checksum(number[:-1])]

    @staticmethod
    def calculate_checksum(numbers):
        cumulative_sum = 0

        # for idx, num in enumerate(numbers[::-1]):
        #     if idx % 2 == 0:
        #         if num * 2 > 9:
        #             # cumulative_sum += sum(map(int, str(num*2))) # "16" -> "1", "6" mapped to int -> 1, 6 -> sum() -> 7
        #             # 16 -> 7 -> 16 - 9
        #             # 13 -> 4 -> 13 - 9
        #             cumulative_sum += num * 2 - 9
        #         else:
        #             cumulative_sum += num * 2
        #     else:
        #         cumulative_sum += num

        toggle = True

        for num in numbers[::-1]:
            n = num * 2 if toggle else num
            toggle = not toggle

            if n > 9:
                cumulative_sum += n - 9
            else:
                cumulative_sum += n

        return 10 - cumulative_sum % 10  # checksum


class CreditCard:
    DIGITS = list(range(9))

    def __init__(self):
        self._number = self.generate()

    def generate(self):
        return choices(self.DIGITS, k=14)

    @property
    def number(self):
        s = "".join(map(str, self._number))  # "12341234"
        return " ".join(re.findall('.{4}', s))  # ["1234", "1234"]


class Visa(VisaMixin, CreditCard):
    pass


class ValidVisa(ValidMixin, VisaMixin, CreditCard):
    pass


class MasterCard(ValidMixin, MasterCardMixin, CreditCard):
    pass


if __name__ == "__main__":
    random_visa = Visa()
    print(f"Random visa: {random_visa.number}".rjust(40))

    valid_visa = ValidVisa()
    print(f"Valid visa: {valid_visa.number}".rjust(40))

    master_card = MasterCard()
    print(f"Valid mastercard: {master_card.number}".rjust(40))
