#
#
#
from dataclasses import dataclass
from collections.abc import Sequence
from random import randint, uniform
from functools import total_ordering
from bisect import insort


@total_ordering
@dataclass(frozen=True)
class JobApplicant:
    applicant_id: str
    years_experience: int
    is_recommended: bool
    first_interview_score: float
    second_interview_score: float

    @property
    def score(self):
        return round(
            self.years_experience * .5 +
            self.is_recommended +
            self.first_interview_score * .5 +
            self.second_interview_score,
            2)

    def __le__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score


class JobApplicantPool(Sequence):
    def __init__(self, *args):
        self._applicants = sorted(list(args))

    def add(self, applicant):
        # self._applicants.append(applicant)
        insort(self._applicants, applicant)

        # figure out the idx where we want to insert the new applicant
        # insert the applicant there using list.insert

    def __getitem__(self, item):
        if type(item) == slice:
            return type(self)(*self._applicants[item])
        elif type(item) == int:
            return self._applicants[item]

        return NotImplemented

    def __len__(self):
        return len(self._applicants)

    def __repr__(self):
        header = f"Applicant Pool\n(Score | ID)\n{'-' * 20}\n"
        return header + "\n".join([
            f"{applicant.score} - {applicant.applicant_id}" for applicant in self._applicants
        ])


def generate_random_applicants(n=10):
    return [
        JobApplicant(
            applicant_id=str(randint(10000, 90000)),
            years_experience=randint(0, 10),
            is_recommended=bool(randint(0, 1)),
            first_interview_score=round(uniform(1.0, 10.0), 2),
            second_interview_score=round(uniform(1.0, 10.0), 2)
        ) for _ in range(n)
    ]


if __name__ == "__main__":
    jab = JobApplicantPool(*generate_random_applicants())
    print(jab)

    new_applicant = generate_random_applicants(1)[0]
    print(f"New applicant score: {new_applicant.score}")

    jab.add(new_applicant)

    print(jab)
