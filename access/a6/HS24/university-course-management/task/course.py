#!/usr/bin/env python3

from task.professor import Professor
from task.student import Student


class Course:

    def __init__(self, course_code: str, course_name: str, professor: Professor):
        pass

    def add_student(self, student: Student) -> int:
        pass

    def get_students(self) -> list:
        pass

    def remove_student(self, student_id: str) -> int:
        pass

    def get_details(self) -> tuple:
        pass
