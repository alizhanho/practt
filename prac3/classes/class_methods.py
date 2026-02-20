class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 60


student1 = Student("Islam", 75)
print(student1.is_passing())