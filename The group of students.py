#Create a class that describes the person (create a method that outputs information about the person).
#Based on it, create the Student class (override the information output method).
#Create a Group class whose instance consists of objects of the Student class.
#Implement methods for adding, removing a student, and a method for searching for a student by last name.
#The student search method must return an instance of the Student class if the student is in the group,
# otherwise - None.
#Define a str() method for the group to return a list of students as a string.
#13.1
from typing import Optional


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"Student: {self.gender}, {self.age}, {self.first_name}, {self.last_name}, {self.record_book}"


class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        sorted_students = sorted(self.group, key=lambda student: student.last_name)
        all_students = "\n".join(str(student) for student in sorted_students)
        return f"Number: {self.number}\n{all_students}"


if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('gr')
    gr.add_student(st2)
    gr.add_student(st1)

    print(gr)

    assert str(gr.find_student('Jobs')) == str(st1), 'Тест 1'
    assert gr.find_student('Jobs2') is None, 'Тест 2'
    assert isinstance(gr.find_student('Jobs'), Student), 'The search method must return an instance of the class'

    gr.delete_student('Taylor')
    print(gr)

    gr.delete_student('Taylor')