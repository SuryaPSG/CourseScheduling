"""
This Python script is used to Handle the Custom Written Course Full Exception
Author:Surya
"""
from src.enums.Constants import Constants


class CourseFullException(Exception):

    def __init__(self):
        print(Constants.COURSE_FULL_ERROR)
        pass
