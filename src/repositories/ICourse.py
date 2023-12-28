"""
Interface to provide all the functionalities of Course allotments
Author: Surya
"""
from src.entities.Employee import Employee
from src.entities.Course import Course


class ICourse:

    def save(self, course: Course):
        pass

    def find_by_offering_name(self, course_offering_name: str):
        pass

    def find_by_course_name(self, course_name: str):
        pass

    def find_all(self):
        pass

    def delete_employee(self, course: Course, employee: Employee):
        pass

    def is_seat_available(self, course_offering_name: str):
        pass

    def get_course_by_offering_name(self, course_offering_name: str):
        pass

    def add_employees(self, offering: str, employee: Employee):
        pass

    def find_allotment_by_offering(self, offering: str):
        pass
