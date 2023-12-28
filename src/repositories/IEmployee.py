"""
Interface to provide all the functionalities of Employee Enrollments
Author: Surya
"""
from src.entities.Employee import Employee


class IEmployee:
    def save(self, employee: Employee):
        pass

    def find_by_registration_number(self, registration_num: str):
        pass

    def find_all(self):
        pass
