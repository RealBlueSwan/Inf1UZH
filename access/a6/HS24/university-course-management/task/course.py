#!/usr/bin/env python3

from professor import Professor
from student import Student


class Course():

    def __init__(self, course_code: str, course_name: str, professor: Professor):
       self.course_code = course_code
       self.course_name = course_name
       self.professor = professor
       self.students = []

    def add_student(self, student: Student) -> int:

        if student in self.students:
            raise ValueError("Student already enroled!")
        
        self.students.append(student)
        return len(self.students)

    def get_students(self) -> list:
        return [Student.get_details(student) for student in self.students]

    def remove_student(self, student_id: str) -> int:

        if student_id not in [Student.get_details(student)[2] for student in self.students]:
            raise ValueError(f"Student_id: {student_id} not enrolled")

        if not self.students:
            raise ValueError("No students enrolled!")
        
        for student in self.students:
            if Student.get_details(student)[2] == student_id:
                self.students.remove(student)
                return len(self.students)
        
        return ValueError(f"Student_id: {student_id} not enrolled")

    def get_details(self) -> tuple:
        return (self.course_code, self.course_name, Professor.get_details(self.professor), len(self.students))
        