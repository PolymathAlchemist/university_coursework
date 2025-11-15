"""
CIS245-T303 Introduction to Programming
Instructor: Dr. Sasan Azazian
Assignment: M10: Assignment - Python Classes Program
Author: Eric J. Turman
Date: 2025-11-11
Email: ejturman@my365.bellevue.edu

This program creates a student class that implements the class diagram
provided in the instructions and calculates a student's cumulative GPA.
Then asks for the student's concentration of study.

The program uses the methods of the base student class and a derived
declared student subclass to accomplish the following:

* Prompt the user for the student's first name, last name, and optional
  declared concentration. If the user presses Enter with no input, the
  concentration is automatically assigned as "NA".
* Create a declared student class that inherits from the student class.
* Create a student object by passing the first and last name to the
  __init__ method.
* Create a declared student object by passing the concentration to its
  __init__ method.
* Create a loop that prompts the user for the credits and grade of each
  completed course.
* After the user ends the loop, display the student's cumulative GPA
  and determine the student's academic year based on credits earned:
    - First year:     <= 33 credits
    - Second year:    <= 66 credits
    - Third year:     <= 96 credits
    - Fourth year:    < 130 credits
    - Multi-year:     >= 130 credits

For simplicity, all classes are kept within a single script.

The program emphasizes robust input validation using regular expressions,
modular design with reusable functions, and clear documentation practices.

To improve data organization and maintainability, this program also uses:
* Enums and dataclasses — special Python classes that provide structured
  data definitions and safe, fixed-choice values.
* Decorators:
    - @overload to begin generalizing and extending the get_data function.
    - @dataclass to practice clean and safe data-structure design.

These techniques are explored with the goal of writing clearer, safer,
and more maintainable code that is friendly to static code analysis.
"""

import re
import difflib
import textwrap
from collections.abc import Collection
from enum import Enum
from dataclasses import dataclass
from typing import (
    Any,
    Final,
    overload,
)


# ========================================================================
# Classes
# ========================================================================
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
        self.student_year = ""


    def add_credits_and_grade(
            self,
            course_credits: int,
            letter_grade: str,
    ) -> None:
        """
        Add the credits on the course and the letter grade after
            converting it to an integer.
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
        """
        Calculate the student's cumulative GPA.

        Returns
        -------
        float
            The GPA computed as total grade points divided by total
            credits, rounded to two decimal places. If the student has not
            completed any credits, the GPA defaults to 0.0.
        """
        if self.credit_load == 0:
            return 0.0
        return round(self.grade_points / self.credit_load, 2)


    def get_credit_load(self) -> int:
        return self.credit_load


    def get_student_year(self) -> str:
        """
        Determine the student's academic year based on total earned
        credits.

        Returns
        -------
        str
            A string describing the student's year:
            "first year" (<= 33 credits),
            "second year" (<= 66 credits),
            "third year" (<= 96 credits),
            "fourth year" (< 130 credits),
            or "multi-year" (>= 130 credits).

        Raises
        ------
        ValueError
            If credit_load invalid.
        """
        match self.credit_load:
            case credits if credits <= 33:
                return "first year"
            case credits if credits <= 66:
                return "second year"
            case credits if credits <= 96:
                return "third year"
            case credits if credits < 130:
                return "fourth year"
            case credits if credits >= 130:
                return "multi-year"
            case _:
                raise ValueError(f"Invalid credit load: {self.credit_load}")


class DeclaredStudent(Student):
    """
    Extension of Student that includes a declared academic concentration.

    Attributes
    ----------
    concentration: str
        The student's declared program of study (e.g., 'Cybersecurity').
        May be 'NA' if the student is undeclared.
    """
    def __init__(
            self,
            first_name: str,
            last_name: str,
            concentration: str
    ):
        super().__init__(
            first_name,
            last_name
        )
        self.concentration = concentration


    def get_concentration(self) -> str:
        return self.concentration


class Degree(Enum):
    """Supported academic degree abbreviations."""
    BS = "BS"
    MS = "MS"
    MBA = "MBA"
    MINOR = "Minor"
    AS = "AS"
    BAS = "BAS"
    CERT = "CERT"
    DBA = "DBA"
    MHA = "MHA"
    MPS = "MPS"
    PHD = "PHD"
    MPM = "MPM"
    BA = "BA"
    MA = "MA"
    UNDEFINED = "NA"


class Location(Enum):
    """Supported locations of where program is located."""
    ON_CAMPUS = "On campus"
    ONLINE = "Online"
    BOTH = "On campus & online"
    UNDEFINED = "NA"


@dataclass (frozen=True)
class ProgramData:
    """
    Provides an immutable structure to describe the list of
    academic programs and information about them

    Attributes
    ----------
    degree: tuple[Degree,...]
        One or more degree of the program (e.g., 'BS', 'MS', 'MBA',) based
        on the Degree enum list.
    location: Location
        Where classes are held based on the Location enum list
    """
    degree: tuple[Degree,...]
    location: Location

# ========================================================================
# Named Constants
# ========================================================================

INTRO_MESSAGE: Final[str] = (
    "Welcome to 'Grade-E-us' the GPA calculator!\n"
    "Follow the instructions and I will give the student's GPA!\n"
    "Enter now and I will divulge their credit load, what year they are and\n"
    "their area of academic concentration."
)

FULL_NAME_INPUT: Final[str] = (
    "Please enter the Student's full name (middle names will be ignored).\n"
    "(At least first and last is required): "
)

FULL_NAME_RE: Final[re.Pattern[str]] = re.compile(
    rf"""
    ^                   # Start anchor.
    (?!.*[\s]{{2}})          # Two space not allowed anywhere.
    [A-Z]               # Initial capitalization .
    [a-zA-Z'.-]+        # Acceptable characters .
    (?:                 # Option to use the () enclosed tokens.
        [\s]             # Exactly one literal space
        [A-Z]           # Initial capitalization.
        [a-zA-Z'.-]+    # Acceptable characters
    )+                  # Previous token quantifier 1 to unlimited times.
    $                   # End anchor.
    """,
    re.VERBOSE
)

FULL_NAME_ERROR: Final[str] = (
    "Both first and last name are required. First letter of names must be "
    "capitalized. Only letters, apostrophes ('), periods (.), "
    "and hyphens (-) are accepted. "
    "Middle initials are fine, but must be followed by a period. "
    "Single space between names."
)

CREDITS_INPUT: Final[str] = (
    "Please enter the number of credits for the course. 1-99: "
)

CREDITS_RE: Final[re.Pattern[str]] = re.compile(r"^[1-9]\d?$")

CREDITS_ERROR: Final[str] = (
    "Only whole values from 1 to 99 are accepted."
)

GRADE_INPUT: Final[str] = (
    "Please enter the letter grade for the course. (A, B, C, D, or F): "
)

GRADE_RE: Final[re.Pattern[str]] = re.compile(r"^[ABCDF]$", re.IGNORECASE)

GRADE_ERROR: Final[str] = (
    "Only A, a, B, b, C, c, D, d, F, or f are accepted."
)

CONTINUE_INPUT: Final[str] = "Add another course? (y/yes, n/no): "

YES_NO_RE: Final[re.Pattern[str]] = re.compile(r"^(?:y|yes|n|no)$", re.IGNORECASE)

YES_NO_ERROR: Final[str] = "Only y, yes, n, no are accepted."


PROGRAM_INPUT: Final[str] = (
    "Please enter the student concentration area. For a list of programs, "
    "enter L\nIf the student is undeclared, press ENTER or type NA: "
)

# Auto-generated dictionary of program (concentration) titles and
#   degree and location information compiled
#   from https://www.bellevue.edu/degrees and reformatted into a
#   dictionary of ProgramData objects using ChatGPT 5.1
PROGRAM_DATA: Final[dict[str, ProgramData]] = {
    "Accounting": ProgramData(
        (Degree.BS, Degree.MS, Degree.MINOR),
        Location.BOTH,
    ),
    "Acquisition and Contract Management": ProgramData(
        (Degree.MS,),
        Location.ONLINE,
    ),
    "Athletic Coaching": ProgramData(
        (Degree.MINOR,),
        Location.ON_CAMPUS,
    ),
    "Behavioral Science": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Biology": ProgramData(
        (Degree.BS, Degree.MINOR),
        Location.ON_CAMPUS,
    ),
    "Business": ProgramData(
        (Degree.AS,),
        Location.BOTH,
    ),
    "Business (Cohort)": ProgramData(
        (Degree.BS,),
        Location.BOTH,
    ),
    "Business Administration": ProgramData(
        (Degree.BS, Degree.MBA, Degree.MINOR),
        Location.BOTH,
    ),
    "Business Administration (Cohort)": ProgramData(
        (Degree.MBA,),
        Location.BOTH,
    ),
    "Business Analysis and Management": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Business Analytics": ProgramData(
        (Degree.BS, Degree.MS),
        Location.BOTH,
    ),
    "Business Management and Leadership": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Business and Professional Communication": ProgramData(
        (Degree.MA,),
        Location.ONLINE,
    ),
    "Chemistry": ProgramData(
        (Degree.MINOR,),
        Location.ON_CAMPUS,
    ),
    "Child, Youth, and Family Studies": ProgramData(
        (Degree.MS,),
        Location.BOTH,
    ),
    "Clinical Mental Health Counseling": ProgramData(
        (Degree.MS,),
        Location.ONLINE,
    ),
    "Communication Studies": ProgramData(
        (Degree.BA, Degree.MINOR),
        Location.BOTH,
    ),
    "Computer Information Systems": ProgramData(
        (Degree.BAS, Degree.BS, Degree.MS, Degree.MINOR),
        Location.BOTH,
    ),
    "Computer Science": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Criminal Justice": ProgramData(
        (Degree.BS, Degree.MS, Degree.MINOR),
        Location.BOTH,
    ),
    "Cybersecurity": ProgramData(
        (Degree.BS, Degree.MS),
        Location.BOTH,
    ),
    "Data Science": ProgramData(
        (Degree.BS, Degree.MS),
        Location.ONLINE,
    ),
    "Doctor of Business Administration": ProgramData(
        (Degree.DBA,),
        Location.ONLINE,
    ),
    "Education (Elementary Endorsement)": ProgramData(
        (Degree.BS,),
        Location.ON_CAMPUS,
    ),
    "Education (Secondary)": ProgramData(
        (Degree.BS,),
        Location.ON_CAMPUS,
    ),
    "Emergency Management": ProgramData(
        (Degree.BS, Degree.MS),
        Location.ONLINE,
    ),
    "Finance": ProgramData(
        (Degree.BS,),
        Location.BOTH,
    ),
    "Financial Planning": ProgramData(
        (Degree.BS, Degree.MS),
        Location.BOTH,
    ),
    "Graphic Design": ProgramData(
        (Degree.BA,),
        Location.ONLINE,
    ),
    "Graphic Design - Print": ProgramData(
        (Degree.MINOR,),
        Location.ONLINE,
    ),
    "Graphic Design - Web": ProgramData(
        (Degree.MINOR,),
        Location.ONLINE,
    ),
    "Health and Human Performance": ProgramData(
        (Degree.BS,),
        Location.ON_CAMPUS,
    ),
    "Health Science": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Healthcare Administration": ProgramData(
        (Degree.MHA,),
        Location.ONLINE,
    ),
    "Healthcare Management": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "History": ProgramData(
        (Degree.BS, Degree.MINOR),
        Location.BOTH,
    ),
    "Hospitality Management": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Human Resource Strategic Management": ProgramData(
        (Degree.MS,),
        Location.BOTH,
    ),
    "Human Services": ProgramData(
        (Degree.MA,),
        Location.ONLINE,
    ),
    "Industrial and Organizational Psychology": ProgramData(
        (Degree.MS,),
        Location.ONLINE,
    ),
    "Information Technology": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Instructional Design and Technology": ProgramData(
        (Degree.MS,),
        Location.ONLINE,
    ),
    "Intelligence and Security Studies": ProgramData(
        (Degree.BS, Degree.MS),
        Location.ONLINE,
    ),
    "International Business Administration": ProgramData(
        (Degree.BS,),
        Location.BOTH,
    ),
    "Interdisciplinary": ProgramData(
        (Degree.MINOR,),
        Location.BOTH,
    ),
    "Kinesiology": ProgramData(
        (Degree.BS,),
        Location.ON_CAMPUS,
    ),
    "Leadership": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Legal Studies": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Management": ProgramData(
        (Degree.BS, Degree.MS),
        Location.ONLINE,
    ),
    "Management and Leadership": ProgramData(
        (Degree.MS,),
        Location.ONLINE,
    ),
    "Management Information Systems": ProgramData(
        (Degree.BS, Degree.MS),
        Location.BOTH,
    ),
    "Management of Human Resources": ProgramData(
        (Degree.BS,),
        Location.BOTH,
    ),
    "Marketing": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Mathematics": ProgramData(
        (Degree.BS, Degree.MINOR),
        Location.BOTH,
    ),
    "Mental Health Technician Certificate": ProgramData(
        (Degree.CERT,),
        Location.ONLINE,
    ),
    "Multidisciplinary Studies": ProgramData(
        (Degree.AS,),
        Location.ONLINE,
    ),
    "Nursing (RN to BSN)": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Organizational Communication": ProgramData(
        (Degree.MINOR,),
        Location.BOTH,
    ),
    "Organizational Leadership": ProgramData(
        (Degree.MS,),
        Location.BOTH,
    ),
    "People and Business Leadership Essentials": ProgramData(
        (Degree.CERT,),
        Location.ONLINE,
    ),
    "Ph.D. Human Capital Management": ProgramData(
        (Degree.PHD,),
        Location.ONLINE,
    ),
    "Professional Studies": ProgramData(
        (Degree.MPS,),
        Location.BOTH,
    ),
    "Project Management": ProgramData(
        (Degree.BS, Degree.MPM),
        Location.ONLINE,
    ),
    "Psychology": ProgramData(
        (Degree.BA, Degree.BS, Degree.MINOR),
        Location.BOTH,
    ),
    "Public Health": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Software Development": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Sport Management": ProgramData(
        (Degree.BA, Degree.BS, Degree.MA, Degree.MINOR),
        Location.BOTH,
    ),
    "Strategic Finance": ProgramData(
        (Degree.MS,),
        Location.BOTH,
    ),
    "Supply Chain Management": ProgramData(
        (Degree.MS,),
        Location.ONLINE,
    ),
    "Supply Chain and Logistics Management": ProgramData(
        (Degree.BS,),
        Location.BOTH,
    ),
    "Supply Chain, Transportation and Logistics Management": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Sustainability Management": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
    "Tax": ProgramData(
        (Degree.MINOR,),
        Location.BOTH,
    ),
    "Teaching": ProgramData(
        (Degree.MA,),
        Location.ONLINE,
    ),
    "Threat Assessment and Management": ProgramData(
        (Degree.MS,),
        Location.ONLINE,
    ),
    "Web Development": ProgramData(
        (Degree.BS,),
        Location.ONLINE,
    ),
}

PROGRAM_ERROR: Final[str] = (
    "Not an available concentration area."
)


# ========================================================================
# Logic functions
# ========================================================================
@overload
def get_data(
        input_message: str,
        match_pattern: re.Pattern[str],
        error_message: str,
        na: bool = False
) -> str:
    ...


@overload
def get_data(
        input_message: str,
        match_pattern: Collection[str],
        error_message: str,
        na: bool = False
) -> str:
    ...


@overload
def get_data(
        input_message: str,
        match_pattern: dict[str,Any],
        error_message: str,
        na: bool = False
) -> str:
    ...


def get_data(
        input_message: str,
        match_pattern: re.Pattern[str] | Collection[str] | dict[str,Any],
        error_message: str,
        na: bool = False
) -> str:
    """
    Get information is a modular input validation function that supports
    three kinds of validation patterns to ensure safe and correct
    user input.
    * Case 1: Regular expressions (re.Pattern)
        - Input must match the regex pattern
    * Case 2: Collection of strings (Collection[str])
        - Input matched against a whitelist of strings.
        - Suggests a fuzzy match against a whitelist of strings.
    * Case 3: Dictionary of string keys (dict[str,Any])
        - Input matched against a whitelist of dictionary keys.
        - Suggests a fuzzy match against a whitelist of dictionary keys.

    Parameters
    ----------
    input_message: str
        Let the user know what information to type in.
    match_pattern: Overloaded parameter:
        re.Pattern[str] | Collection[str] | dict[str,Any]
    error_message
        Message to let the user know what they are typing wrong.
    na: bool
        If True, return "NA" instead of raising an error if
        an empty string or "NA" is entered.
    Returns
    -------
    value: str
        Validated input string value.
    Raises
    -------
    TypeError
        If match_pattern is not a supported type.
    RunTimeError if receives a match_pattern if it reaches an
        unexpected state (which should be impossible).
    Notes
    -------
    This function will loop until it receives a valid input
    """
    while True:
        value = input(input_message).strip()
        if na and (value.lower() == "na" or value.lower() == ""):
            return "NA"

        # ----------------------------------------------------------------
        # Case 1: Regular Expression
        # ----------------------------------------------------------------
        if isinstance(match_pattern, re.Pattern):
            try:
                if not match_pattern.fullmatch(value):
                    raise ValueError(error_message)
                return value
            except ValueError as error:
                print(textwrap.fill(
                    f"{'!'*79}\n{error}\n{'!'*79}",
                    width=79
                ))

        # ----------------------------------------------------------------
        # Case 2: Collection of Strings
        # ----------------------------------------------------------------
        elif (
                isinstance(match_pattern, Collection)
                and not isinstance(match_pattern, dict)
                and not isinstance(match_pattern, str)
                and all(isinstance(item, str) for item in match_pattern
        )):
            if value.upper() == "L":
                valid_input_message = ", ".join(match_pattern)
                print(textwrap.fill(valid_input_message, width=79))
                continue
            else:
                try:
                    if value in match_pattern:
                        return value
                    close_matches = difflib.get_close_matches(
                        value,
                        match_pattern,
                        n=1
                    )
                    if close_matches:
                        use_close = get_data(
                            f"Did you mean '{close_matches[0]}'?",
                            YES_NO_RE,
                            YES_NO_ERROR
                        )
                        if use_close[0].upper() == "Y":
                            return close_matches[0]
                        else:
                            continue
                    raise ValueError(error_message)
                except ValueError as error:
                    print(textwrap.fill(
                    f"{'!'*79}\n{error}\n{'!'*79}",
                    width=79
                ))

        # ----------------------------------------------------------------
        # Case 3: Dictionary
        # ----------------------------------------------------------------
        elif isinstance(match_pattern, dict):
            valid_keys = list(match_pattern.keys())
            if value.upper() == "L":
                valid_input_message = ", ".join(valid_keys)
                print(textwrap.fill(valid_input_message, width=79))
                continue
            else:
                try:
                    if value in valid_keys:
                        return value
                    close_matches = difflib.get_close_matches(
                        value,
                        valid_keys,
                        n=1
                    )
                    if close_matches:
                        use_close = get_data(
                            f"Did you mean '{close_matches[0]}'?",
                            YES_NO_RE,
                            YES_NO_ERROR
                        )
                        if use_close[0].upper() == "Y":
                            return close_matches[0]
                        else:
                            continue
                    raise ValueError(error_message)
                except ValueError as error:
                    print(textwrap.fill(
                    f"{'!'*79}\n{error}\n{'!'*79}",
                    width=79
                ))

        # ----------------------------------------------------------------
        # Fall-through Case: Unexpected match_pattern
        # ----------------------------------------------------------------
        else:
            raise TypeError(
                "match_pattern must be a regular expression pattern, a "
                "collection of strings, or a dictionary with string keys."
            )
    raise RuntimeError("get_data() reached an unexpected state")


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
            YES_NO_RE,
            YES_NO_ERROR
        )
        if continue_grade.upper()[0] == "N":
            break


def main() -> None:
    """
    Main program loop to get a student name, gather credit loads
    and letter grades, calculate the GPA, and display the results.
    """
    print(INTRO_MESSAGE)
    full_name = get_data(
        FULL_NAME_INPUT,
        FULL_NAME_RE,
        FULL_NAME_ERROR
    )
    concentration = get_data(
        PROGRAM_INPUT,
        PROGRAM_DATA,
        PROGRAM_ERROR,
        True
    )
    first_last_name = process_full_name(full_name)
    student1 = DeclaredStudent(
        first_last_name[0],
        first_last_name[1],
        concentration
    )
    build_credit_load_and_grades(student1)
    if concentration == "NA":
        message_tail = "whose concentration is currently undeclared"
    else:
        message_tail = (
            f"who is concentrating on {student1.get_concentration()}"
        )
    print(textwrap.fill(
        f"{'='*79}\n{student1.first_name} {student1.last_name} "
        f"has completed a total of {student1.get_credit_load()} credits and "
        "received a grade point average (GPA) of "
        f"{student1.get_grade_point_average()}. They are a "
        f"{student1.get_student_year()} student {message_tail}."
        , width=79)
    )


if __name__ == '__main__':
    main()
