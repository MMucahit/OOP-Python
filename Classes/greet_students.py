from random import choice

class Student:
    educational_platform = "udemy"
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
    
    def greet(self):
        _greeting = ["Hi, I am", "Hey there, my name is", "Hi. Oh, my name is"]
        greeting = choice(_greeting)
        
        return f"{greeting} {self.name}"

def class_create(names):
    return [Student(name) for name in names]

if __name__ == "__main__":
    names = ["Mucahit", "Yusa", "Samet"]

    print([student.greet() for student in class_create(names)])