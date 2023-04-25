#
#
#
from dataclasses import dataclass
from collections.abc import Sequence
from random import randint, uniform


@dataclass(frozen=True)
class JobApplicant:
    applicant_id: str
    years_experience: int
    is_recommended: bool
    first_interview_score: float
    second_interview_score: float


class JobApplicantPool(Sequence):
    def __init__(self, *args):
        self._applicants = list(args)

    def add(self, applicant):
        self._applicants.append(applicant)

    def __getitem__(self, item):
        if type(item) == slice:
            return type(self)(*self._applicants[item])
        elif type(item) == int:
            return self._applicants[item]

        return NotImplemented

    def __len__(self):
        return len(self._applicants)

    def __repr__(self):
        sorted_applicants = sorted(self._applicants, key=self.score, reverse=True)
        header = f"Applicant Pool\n(Score | ID)\n{'-' * 20}\n"
        return header + "\n".join([
            f"{self.score(applicant)} - {applicant.applicant_id}" for applicant in sorted_applicants
        ])

    @staticmethod
    def score(applicant: JobApplicant):
        return round(
            applicant.years_experience * .5 +
            applicant.is_recommended +
            applicant.first_interview_score * .5 +
            applicant.second_interview_score,
            2)


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
