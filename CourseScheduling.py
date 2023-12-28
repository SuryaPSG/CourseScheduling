"""
This python script is responsible for the actual invocation
Author: Surya
"""
from src.helper.RunCode import RunCode
import sys


class CourseScheduling:

    @staticmethod
    def run_commands():
        try:
            n = len(sys.argv)
            if n == 1:
                raise RuntimeError
            command_line_args = sys.argv[1:]
            RunCode.run(command_line_args)

        except RuntimeError:
            pass


if __name__ == "__main__":
    CourseScheduling.run_commands()
