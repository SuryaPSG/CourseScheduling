"""
This Python Script is to model the employee entity data
Author: Surya
"""

from src.enums.Constants import Constants


class Employee:

    def __init__(self, emp_id: int, name: str, email_id: str, offering: str, register_number: str):
        self.emp_id = emp_id
        self.name = name
        self.email_id = email_id
        self.offering = offering
        self.register_number = register_number

    def get_emp_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def get_email_id(self):
        return self.email_id

    def get_offering(self):
        return self.offering

    def get_register_number(self):
        return self.register_number

    def __str__(self):
        return self.register_number + " " + Constants.ACCEPTED
