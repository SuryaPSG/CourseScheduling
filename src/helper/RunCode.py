"""
This Script invokes the actual execution
Author:Surya
"""
from src.enums.ParametersCount import ParametersCount
from src.exceptions.InputDataException import InputDataException
from src.repositories.CourseRepository import CourseRepository
from src.repositories.EmployeeRepository import EmployeeRepository
from src.services.CourseService import CourseService
from src.services.EmployeeService import EmployeeService
import re


class RunCode:

    @staticmethod
    def execute_add_course_offering_command(tokens, course_service):
        tokens_size = len(tokens)
        if not RunCode.check_parameters(expected=ParametersCount.ADD_COURSE_OFFERING, actual=tokens_size):
            return
        course_name = tokens[1]
        instructor_name = tokens[2]
        date = tokens[3]
        min_employees = int(tokens[4])
        max_employees = int(tokens[5])
        course = course_service.create_course(course_name, instructor_name, date,
                                              min_employees, max_employees)
        if course is not None:
            print(course)

    @staticmethod
    def check_parameters(expected: int, actual: int):
        try:
            if expected != (actual - 1):
                raise InputDataException()
        except InputDataException:
            return False
        else:
            return True

    @staticmethod
    def execute_register_command(tokens, employee_service):
        tokens_size = len(tokens)
        if not RunCode.check_parameters(expected=ParametersCount.REGISTER, actual=tokens_size):
            return
        email_id = tokens[1]
        offering = tokens[2]
        try:
            pattern = r'\w+@\w+.\w+'
            match = re.search(pattern, email_id)
            if match is None:
                raise InputDataException()
            employee = employee_service.register(email_id, offering)
            if employee is not None:
                print(employee)
        except InputDataException:
            pass

    @staticmethod
    def execute_allot_command(tokens, course_service):
        tokens_size = len(tokens)
        if not RunCode.check_parameters(expected=ParametersCount.ALLOT, actual=tokens_size):
            return
        offering = tokens[1]
        allotments = course_service.allot_course(offering)
        if allotments is None:
            return
        for allotment in allotments:
            print(allotment)

    @staticmethod
    def execute_cancel_command(tokens, employee_service):
        tokens_size = len(tokens)
        if not RunCode.check_parameters(expected=ParametersCount.CANCEL, actual=tokens_size):
            return
        reg_num = tokens[1]
        employee_service.cancel_registration(reg_num)

    @staticmethod
    def parse_commands(tokens, course_service, employee_service):
        if tokens[0] == "ADD-COURSE-OFFERING":
            RunCode.execute_add_course_offering_command(tokens, course_service)

        elif tokens[0] == "REGISTER":
            RunCode.execute_register_command(tokens, employee_service)

        elif tokens[0] == "ALLOT":
            RunCode.execute_allot_command(tokens, course_service)

        elif tokens[0] == "CANCEL":
            RunCode.execute_cancel_command(tokens, employee_service)

        else:
            pass

    @staticmethod
    def run(command_line_args: list):
        course_repository = CourseRepository()
        employee_repository = EmployeeRepository()

        course_service = CourseService(course_repository=course_repository)
        employee_service = EmployeeService(course_repository=course_repository, employee_repository=employee_repository)

        input_file = command_line_args[0]

        with open(input_file, mode='r') as f:
            lines = f.readlines()
            for line in lines:
                tokens = line.split()
                RunCode.parse_commands(tokens, course_service, employee_service)
