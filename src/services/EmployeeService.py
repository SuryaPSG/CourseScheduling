"""
This python script provides all the APIs related to Employees
Author:Surya
"""
from src.enums.Constants import Constants
from src.entities.Employee import Employee
from src.repositories.CourseRepository import CourseRepository
from src.repositories.EmployeeRepository import EmployeeRepository


class EmployeeService:

    def __init__(self, course_repository: CourseRepository, employee_repository: EmployeeRepository):
        self.course_repository = course_repository
        self.employee_repository = employee_repository

    def register(self, email_id: str, offering: str):
        e = None
        if self.course_repository.is_seat_available(offering):
            name = email_id.split('@')[0]
            course_name = self.course_repository.get_course_by_offering_name(offering)
            reg_num = 'REG-COURSE-' + name + '-' + course_name
            employee = Employee(emp_id=0, name=name, email_id=email_id, offering=offering,
                                register_number=reg_num)
            e = self.employee_repository.save(employee)
            self.course_repository.add_employees(offering, e)
        return e

    def cancel_registration(self, reg_num):
        employee = self.employee_repository.find_by_registration_number(reg_num)
        if employee is None:
            return
        offering = employee.get_offering()
        if offering is None:
            return
        course = self.course_repository.find_by_offering_name(offering)
        if course.get_status() == Constants.NOT_CONFIRMED:
            self.course_repository.delete_employee(course, employee)
            print(reg_num+' '+Constants.CANCEL_ACCEPTED)
        else:
            print(reg_num+' '+Constants.CANCEL_REJECTED)
        return 
