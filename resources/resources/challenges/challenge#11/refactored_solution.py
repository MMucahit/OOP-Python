#
#
#
class ValidatedScore:
    def __init__(self, score=400, score_name=None, min_score=400, max_score=1600):
        self.score = score
        self.score_name = score_name
        self.min_score = min_score
        self.max_score = max_score

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__.get(f"{self.score_name}_{self.name}")

    def __set__(self, instance, value):
        if not type(value) == int:
            raise TypeError("Score must be an integer")

        if not self.min_score <= value <= self.max_score:
            raise ValueError(f"Score must fall between {self.min_score} and {self.max_score}")

        instance.__dict__[f"{self.score_name}_{self.name}"] = value


class SATScore(ValidatedScore):
    def __init__(self, score=400):
        super().__init__(score=score, score_name=self.__class__.__name__, min_score=400, max_score=1600)


class GREScore(ValidatedScore):
    def __init__(self, score=130):
        super().__init__(score=score, score_name=self.__class__.__name__, min_score=130, max_score=340)


class StudentProfile:
    sat = SATScore()
    gre = GREScore()

    def __init__(self, name=None, sat=400, gre=130):
        self.name = name
        self.sat = sat
        self.gre = gre

    def __repr__(self):
        return f"StudentProfile(name='{self.name}', sat={self.sat}, gre={self.gre})"
