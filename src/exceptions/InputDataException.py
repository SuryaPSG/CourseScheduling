"""
This Python script is used to Handle the Custom Written Input Data Exception
Author:Surya
"""
from src.enums.Constants import Constants


class InputDataException(Exception):

    def __init__(self):
        print(Constants.INPUT_DATA_ERROR)
        pass
