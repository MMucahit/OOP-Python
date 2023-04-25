from random import choice


class Student:
    educational_platform = "Udemy"

    def __init__(self, name, age=34):
        self.name = name
        self.age = age

    def greet(self):
        _greetings = [
            "Hi, I'm {}",
            "Hey there, my name is {}",
            "Hi. Oh, my name is {}"
        ]

        greeting = choice(_greetings)

        return greeting.format(self.name)


def class_create(student_names):
    return [Student(name) for name in student_names]


if __name__ == "__main__":
    names = ["Alice", "Brian", "Clayton", "Deirdre", "Elon", "Faye"]

    for student in class_create(names):
        print(student.greet())
