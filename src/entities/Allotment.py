"""
self Python Script is to model the Course wise allotments entity data
Author: Surya
"""
import functools
from src.entities.Employee import Employee
from src.entities.Course import Course


@functools.total_ordering
class Allotment:

    def __init__(self, employee: Employee, course: Course):
        self.employee = employee
        self.course = course

    def __lt__(self, other):
        return self.employee.get_register_number() < other.employee.get_register_number()

    def __gt__(self, other):
        return self.employee.get_register_number() > other.employee.get_register_number()

    def __eq__(self, other):
        return self.employee.get_register_number() == other.employee.get_register_number()

    def __str__(self):
        return (self.employee.get_register_number() + " " + self.employee.get_email_id() + " " +
                self.course.get_offering() + " " + self.course.get_title() + " " + self.course.get_instructor() + " " +
                self.course.get_date() + " " + self.course.get_status())
