class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade})'

def add_student(students, name, age, grade):
    new_student = Student(name, age, grade)
    students.append(new_student)

def display_students(students):
    for student in students:
        print(student)
