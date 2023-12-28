"""
Implementation of the methods from ICourse
Author:Surya
"""

from src.repositories.IEmployee import IEmployee
from src.entities.Employee import Employee


class EmployeeRepository(IEmployee):
    auto_increment = 1

    def __init__(self):
        self.employee_map = dict()

    def save(self, employee: Employee):
        emp = Employee(EmployeeRepository.auto_increment, employee.get_name(), employee.get_email_id(),
                       employee.get_offering(), employee.get_register_number())
        self.employee_map[EmployeeRepository.auto_increment] = emp

        EmployeeRepository.auto_increment += 1
        return emp

    def find_by_registration_number(self, registration_num: str):
        for _, employee in self.employee_map.items():
            if employee.get_register_number() == registration_num:
                return employee
        return None

    def find_all(self):
        return [emp for _, emp in self.employee_map]
