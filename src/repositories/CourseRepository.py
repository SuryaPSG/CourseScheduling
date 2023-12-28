"""
Implementation of the methods from ICourse
Author:Surya
"""

from src.repositories.ICourse import ICourse
from src.entities.Employee import Employee
from src.entities.Course import Course
from src.entities.Allotment import Allotment
from src.enums.Constants import Constants


class CourseRepository(ICourse):
    auto_increment = 1

    def __init__(self):
        self.course_map = dict()

    def save(self, course: Course):
        cor = Course(CourseRepository.auto_increment, course.get_title(), course.get_instructor(), course.get_date(),
                     course.get_min_employees(), course.get_max_employees())
        self.course_map[CourseRepository.auto_increment] = cor
        CourseRepository.auto_increment += 1
        return cor

    def find_by_offering_name(self, course_offering_name: str):
        for _, course in self.course_map.items():
            if course.get_offering() == course_offering_name:
                return course
        return None

    def find_by_course_name(self, course_name: str):
        for _, course in self.course_map.items():
            if course.get_title() == course_name:
                return course
        return None

    def find_all(self):
        return [cor for _, cor in self.course_map]

    def delete_employee(self, course: Course, employee: Employee):
        course.remove_employee(employee)
        return

    def is_seat_available(self, course_offering_name: str):
        course = self.find_by_offering_name(course_offering_name)
        if course is None:
            return False
        if course.get_employee_count() < course.get_max_employees() and course.get_status() == Constants.NOT_CONFIRMED:
            return True
        else:
            print(Constants.COURSE_FULL_ERROR)
        return False

    def get_course_by_offering_name(self, course_offering_name: str):
        course = self.find_by_offering_name(course_offering_name)
        return None if course is None else course.get_title()

    def add_employees(self, offering: str, employee: Employee):
        course = self.find_by_offering_name(offering)
        if course is None:
            return
        course.add_employee(employee)
        return

    def find_allotment_by_offering(self, offering: str):
        course = self.find_by_offering_name(offering)
        employees = course.get_employees()
        allotments = []

        for employee in employees:
            allotment = Allotment(employee, course)
            allotments.append(allotment)

        allotments.sort()
        return allotments
