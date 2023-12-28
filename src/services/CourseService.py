"""
This python script provides all the APIs related to courses
Author:Surya
"""
from src.enums.Constants import Constants
from src.entities.Course import Course
from src.repositories.CourseRepository import CourseRepository


class CourseService:

    def __init__(self, course_repository: CourseRepository):
        self.course_repository = course_repository

    def create_course(self, course_name: str, instructor_name: str, date: str, min_employees: int, max_employees: int):
        course = self.course_repository.find_by_course_name(course_name)
        if course is not None:
            course.reset_attributes(min_employees, max_employees)
            return course
        else:
            course = Course(course_id=0, title=course_name, instructor=instructor_name, date=date,
                            min_employees=min_employees, max_employees=max_employees)
            return self.course_repository.save(course)

    def allot_course(self, offering: str):
        course = self.course_repository.find_by_offering_name(offering)
        if course.get_min_employees() <= course.get_employee_count():
            course.set_status(Constants.COURSE_ALLOTTED)
        else:
            course.set_status(Constants.COURSE_CANCELED)
        return self.course_repository.find_allotment_by_offering(offering)
