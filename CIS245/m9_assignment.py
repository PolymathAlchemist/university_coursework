"""
CIS245-T303 Introduction to Programming
Instructor: Dr. Sasan Azazian
Assignment: M9: Assignment - Python Classes Program
Author: Eric J. Turman
Date: 2025-11-09
Email: ejturman@my365.bellevue.edu

This program
Create a student class that implements the following class diagram that will
calculate and display student cumulative GPA: Student Class Diagram.

This program will then use the methods of the student class to accomplish
the following:

* Prompt the user for the first and last name of the student.
* Create a student object by passing the first and last name to
    the __init__ method.
* Create a loop that prompts the user for the following: The credits and
    grade for each course the student has taken.
* Once the user ends the loop display the student’s cumulative GPA.

For simplicity, the class is being kept within the same script

The program emphasizes robust input validation using regular expressions,
modular design with reusable functions, and consistent NumPy
documentation practices.
"""


import re
import textwrap
from typing import Final

# ====================
# Named Constants
# ====================

INTRO_MESSAGE: Final[str] = (
    "Welcome to 'Grade-E-us' the GPA calculator!\n"
    "Follow the instructions and I will give the student's GPA!\n"
)

FULL_NAME_INPUT: Final[str] = (
    "Please enter the Student's full name (middle names will be ignored).\n"
    "(At least first and last is required): "
)

FULL_NAME_RE: Final[re.Pattern[str]] = re.compile(
    rf"""
    ^                   # Start anchor.
    (?!.*[ ]{2})          # Two space not allowed anywhere.
    [A-Z]               # Initial capitalization .
    [a-zA-Z'.-]+        # Acceptable characters .
    (?:                 # Option to use the () enclosed tokens.
        [ ]             # Exactly one literal space
        [A-Z]           # Initial capitalization. (ONE Explicit space before)
        [a-zA-Z'.-]+    # Acceptable characters
    )+                  # Previous token quantifier 1 to unlimited times.
    $                   # End anchor.
    """,
    re.VERBOSE
)

FULL_NAME_ERROR: Final[str] = (
    "Both first and last name are required. First letter of names must be "
    "capitalized.\n Only letters, apostrophes ('), periods (.), "
    "and hyphens (-) are accepted.\n"
    "Middle initials are fine, but must be followed by a period."
)

CREDITS_INPUT: Final[str] = (
    "Please enter the number of credits for the course.\n"
    "1, 2, 3, 4, 5, 6, 7 ,8 ,or 9: "
)

CREDITS_RE: Final[re.Pattern[str]] = re.compile(r"^[1-9]d?$")

CREDITS_ERROR: Final[str] = (
    "Only whole values of 1, 2, 3, 4, 5, 6, 7, 8, or 9 are accepted."
)

GRADE_INPUT: Final[str] = (
    "Please enter the letter grade for the course.\n"
    "(A, B, C, D, or F): "
)

GRADE_RE: Final[re.Pattern[str]] = re.compile(r"^[ABCDF]$", re.IGNORECASE)

GRADE_ERROR: Final[str] = (
    "Only A, a, B, b, C, c, D, d, F, or f are accepted."
)

CONTINUE_INPUT: Final[str] = "Add another course? (y/yes, n/no): "

CONTINUE_RE: Final[re.Pattern[str]] = re.compile(r"^(?:y|yes|n|no)$", re.IGNORECASE)

CONTINUE_ERROR: Final[str] = "Only y, yes, n, no are accepted."

# ====================
# Classes
# ====================
class Student:
    """
    Represent a student and track cumulative grade information.

    Attributes
    ----------
    first_name : str
        The student's first name.
    last_name : str
        The student's last name.
    grade_points : int
        Total accumulated grade points from all courses.
    credit_load : int
        Total number of credits attempted.
    """

    def __init__(
            self, first_name: str,
            last_name: str
    ) -> None:
        """
        Initialize a new Student instance.

        Parameters
        ----------
        first_name : str
            The student's first name.
        last_name : str
            The student's last name.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.grade_points = 0
        self.credit_load = 0


    def add_credits_and_grade(
            self,
            course_credits: int,
            letter_grade: str,
    ) -> None:
        """
        Add the credits on the course and the letter grade after converting
            it to an integer.
        Parameters
        ----------
        course_credits: int
            The number of credits for the course.
        letter_grade: str
            The letter grade for the course (A, B, C, D, or F).
        """
        self.credit_load += course_credits
        match letter_grade.upper():
            case "A":
                self.grade_points += course_credits * 4
            case "B":
                self.grade_points += course_credits * 3
            case "C":
                self.grade_points += course_credits * 2
            case "D":
                self.grade_points += course_credits * 1
            case "F":
                self.grade_points += course_credits * 0
            case _:
                raise ValueError(f"Invalid grade: {letter_grade}")

    def get_grade_point_average(self) -> float:
        if self.credit_load == 0:
            return 0.0
        return round(self.grade_points / self.credit_load, 2)

    def get_credit_load(self) -> int:
        return self.credit_load


# ====================
# Logic functions
# ====================
def get_data(
        input_message: str,
        re_pattern: re.Pattern[str],
        error_message: str
) -> str:
    """
    Get information is a modular input validation function that uses
    regular expressions to ensure safe and correct user input.

    Parameters
    ----------
    input_message: str
        Let the user know what information to type in.
    re_pattern: re.Pattern[str] regular expression pattern
        Regular expression pattern to filter for correct input
    error_message
        Message to let the user know what they are typing wrong.
    Returns
    -------
    value: str
        Validated input string value.
    """
    while True:
        try:
            value = input(input_message).strip()
            if not re_pattern.fullmatch(value):
                raise ValueError(error_message)
            return value
        except ValueError as error:
            print(f"{'!'*79}\n{error}\n{'!'*79}")


def process_full_name(full_name) -> tuple[str, str]:
    """
    Process full name input splitting it into first and last name
    Parameters
    ----------
    full_name
        Full name input string can contain any number of middle names.

    Returns
    -------
    a tuple of first name and last name.
        first_name: str
            first name at [0]
        last_name: str
            last name at [1]
    """
    name_list = full_name.split()
    first_name = name_list[0]
    last_name = name_list[-1]
    return first_name, last_name


def build_credit_load_and_grades(student1: Student) -> None:
    """
    Build credit load and grade information for the given student.

    The function loops, collecting course credits and letter grades,
    until the user enters 'n' or 'no' to stop.
    ----------
    student1: Student
        Student instance containing full name and last name and whose
        GPA record will be updated.
    """
    while True:
        course_credits = int(get_data(
            CREDITS_INPUT,
            CREDITS_RE,
            CREDITS_ERROR
        ))
        course_grade = get_data(
            GRADE_INPUT,
            GRADE_RE,
            GRADE_ERROR
        )
        student1.add_credits_and_grade(course_credits, course_grade)
        continue_grade = get_data(
            CONTINUE_INPUT,
            CONTINUE_RE,
            CONTINUE_ERROR
        )
        if continue_grade.upper()[0] == "N":
            break


def main() -> None:
    """
    Main program loop to get a student name, gather credit loads
    and letter grades, calculate the GPA, and display the results.
    """
    print(INTRO_MESSAGE)
    full_name = get_data(FULL_NAME_INPUT, FULL_NAME_RE, FULL_NAME_ERROR)
    first_last_name = process_full_name(full_name)
    student1 = Student(first_last_name[0], first_last_name[1])
    build_credit_load_and_grades(student1)
    print(textwrap.fill(f"{student1.first_name} {student1.last_name} "
        f"took on a total of {student1.get_credit_load()} credits and "
        "received a grade point average (GPA) of "
        f"{student1.get_grade_point_average()}."
        , width=79)
    )


if __name__ == '__main__':
    main()
