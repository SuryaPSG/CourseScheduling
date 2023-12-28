"""
This provides the testing functionality and checks some unit test cases
Author: Surya
"""

import unittest
from src.helper.RunCode import RunCode
import sys
from filecmp import cmp


class CourseCourseScheduleTest(unittest.TestCase):

    def test_application(self):
        input_file_path = 'resources/input.txt'
        actual_output_file_path = 'resources/actual_output.txt'
        expected_output_file_path = 'resources/expected_output.txt'
        orig_stdout = sys.stdout
        with open('resources/actual_output.txt', mode='w+') as f:
            sys.stdout = f
            RunCode.run([input_file_path])
            sys.stdout = orig_stdout
        self.assertTrue(cmp(actual_output_file_path, expected_output_file_path))


if __name__ == "__main__":
    unittest.main()
