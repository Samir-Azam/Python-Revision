# property decorator

class Student:

    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1<=age<=5:
            self._age = age
        else :
            raise ValueError("Student is too older for nursery")

std = Student(2)

std.age = 4
print(std.age)
std.age = 5
print(std.age)

