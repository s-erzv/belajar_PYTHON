class Person:
    def __init__(self, name, age, kelas):
        self.name = name
        self.age = age
        self.kelas = kelas

p1 = Person("Sarah", 17, 12)
print(p1.__dict__)
print("Hello, " + p1.name)
print("Age: " + str(p1.age))
print("Class: " + str(p1.kelas))