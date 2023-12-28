"""
This Python Script is to model the Course entity data
Author: Surya
"""

from src.enums.Constants import Constants
from src.entities.Employee import Employee


class Course:

    def __init__(self, course_id: int, title: str, instructor: str, date: str, min_employees: int, max_employees: int):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.date = date
        self.min_employees = min_employees
        self.max_employees = max_employees
        self.offering = 'OFFERING-'+self.title+'-'+self.instructor
        self.status = Constants.NOT_CONFIRMED
        self.employees = []

    def get_course_id(self):
        return self.course_id

    def get_title(self):
        return self.title

    def get_instructor(self):
        return self.instructor

    def get_date(self):
        return self.date

    def get_min_employees(self):
        return self.min_employees

    def get_max_employees(self):
        return self.max_employees

    def get_offering(self):
        return self.offering

    def get_status(self):
        return self.status

    def get_employee_count(self):
        return len(self.employees)

    def get_employees(self):
        return self.employees

    def set_status(self, status: str):
        self.status = status
        return

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        return

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)
        return

    def reset_attributes(self, min_employees: int, max_employees: int):
        self.min_employees = min_employees
        self.max_employees = max_employees
        self.employees = []
        self.status = Constants.NOT_CONFIRMED

    def __str__(self):
        return self.offering
