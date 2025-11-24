"""
CIS245-T303 Introduction to Programming
Instructor: Dr. Sasan Azazian
Assignment: M7 – Python String Program
Author: Eric J. Turman
Date: 2025-10-26
Email: ejturman@my365.bellevue.edu

This program prompts the user for a string containing a person’s first,
middle, and last names, and then display their
first, middle, and last initials.

The program emphasizes robust input validation using regular expressions,
modular design with reusable functions, and consistent documentation practices.
It employs selected data types from future chapter techniques
(e.g., type hints, regular expressions, and random)
to achieve the input validation that was emphasized.

Data Sources
-----------
Names for this project were compiled from the following sources:
https://www.goodhousekeeping.com/life/parenting/a31401884/gender-neutral-baby-names
https://www.thoughtco.com/most-common-us-surnames-1422656
Manually extracted Web information and formatted by ChatGPT.
"""

import re
from random import randint
from typing import Final


# ====================
# Named Constants
# ====================

INTRODUCTION_MESSAGE: Final[str] = (
    f"{'*'*79}\nYou are still in possession of Kilom-eater's car, but all "
    "that driving\nhas run it out of gas. The engine coughs and sputters "
    "as you pull into\nthe '3G full-service' gas station. With a beaming "
    "smile the pump attendant\nenthusiastically strides over to your "
    "driver's side window and extends his\nhand for payment. Reaching into "
    "Kilom-eater's glove box, you extract a handful\nof soggy bills. As you "
    "press the slimy smackers into his hand, his beaming\nsmile fades "
    "as he pockets the grimy greenback and simply says, \"Oh, you know\n"
    "Kilom-eater,\" and moves to gas up the car, pasta juice dripping from "
    "his\nfingers as he wipes them on an oily pocket-rag. He notices your "
    "surprised\nlook, and smiling says, \"I know what you are thinking "
    "'This guy must be\npsychic.'\" *That's not at all what I was thinking* "
    "you think to yourself.\nHe continues, \"Guss Gas-up Guesser is the name, "
    "gas-up gets me the green and\nguessing while gassing is the game. As you "
    "try to parse that sentence he\nrambles on, \"I'm the proprietor of this "
    "fine establishment, and I bet I can\nguess your initials\" Raising an "
    "eyebrow he posits, \"You look like your name\nis...\" and scratching his "
    "chin he says to you,"
)

LAST_NAMES: Final[list[str]] = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Gonzales",
    "Wilson",
    "Anderson",
    "Thomas",
    "Taylor",
    "Moore",
    "Jackson",
    "Martin",
    "Lee",
    "Perez",
    "Thompson",
    "White",
    "Harris",
    "Sanchez",
    "Clark",
    "Ramirez",
    "Lewis",
    "Robinson",
    "Walker",
    "Young",
    "Allen",
    "King",
    "Wright",
    "Scott",
    "Torres",
    "Nguyen",
    "Hill",
    "Flores",
    "Green",
    "Adams",
    "Nelson",
    "Baker",
    "Hall",
    "Rivera",
    "Campbell",
    "Mitchell",
    "Carter",
    "Roberts",
    "Gomez",
    "Phillips",
    "Evans",
    "Turner",
    "Diaz",
    "Parker",
    "Cruz",
    "Edwards",
    "Collins",
    "Reyes",
    "Stewart",
    "Morris",
    "Morales",
    "Murphy",
    "Cook",
    "Rogers",
    "Gutierrez",
    "Ortiz",
    "Morgan",
    "Cooper",
    "Peterson",
    "Bailey",
    "Reed",
    "Kelly",
    "Howard",
    "Ramos",
    "Kim",
    "Cox",
    "Ward",
    "Richardson",
    "Watson",
    "Brooks",
    "Chavez",
    "Wood",
    "James",
    "Bennet",
    "Gray",
    "Mendoza",
    "Ruiz",
    "Hughes",
    "Price",
    "Alvarez",
    "Castillo",
    "Sanders",
    "Patel",
    "Myers",
    "Long",
    "Ross",
    "Foster",
    "Jimenez"
]

FIRST_NAMES: Final[list[str]] = [
    "Adair",
    "Adrian",
    "Alex",
    "Alva",
    "Amari",
    "Ariel",
    "Archie",
    "Arbor",
    "Artemis",
    "Ash",
    "Aspen",
    "Aster",
    "Aubrey",
    "Azriel",
    "Bailey",
    "Bay",
    "Basil",
    "Bellamy",
    "Bentley",
    "Birch",
    "Blair",
    "Blake",
    "Bowie",
    "Bryce",
    "Campbell",
    "Carey",
    "Cassidy",
    "Cedar",
    "Chandler",
    "Cleo",
    "Clover",
    "Colby",
    "Collins",
    "Courtney",
    "Cruz",
    "Dallas",
    "Dale",
    "Dana",
    "Darcy",
    "Denver",
    "Devon",
    "Drew",
    "Easton",
    "Echo",
    "Egypt",
    "Ellis",
    "Everest",
    "Fallon",
    "Francis",
    "Gale",
    "Gray",
    "Greer",
    "Guadalupe",
    "Harley",
    "Hart",
    "Holland",
    "Hollis",
    "Honor",
    "Hunter",
    "Indigo",
    "Jackie",
    "Jagger",
    "James",
    "Jamie",
    "Jan",
    "Jean",
    "Jesse",
    "Jessie",
    "Jett",
    "Jody",
    "Johnnie",
    "Juniper",
    "Keaton",
    "Keeley",
    "Kelsey",
    "Kendall",
    "Kerry",
    "Kim",
    "Kirby",
    "Kit",
    "Koda",
    "Kris",
    "Lane",
    "Lennox",
    "Leslie",
    "Lindsey",
    "London",
    "Loyal",
    "Lowen",
    "Lux",
    "Luxury",
    "Lynn",
    "Lyric",
    "Mackenzie",
    "Marion",
    "Marley",
    "Marlowe",
    "Merrill",
    "Merritt",
    "Micah",
    "Michel",
    "Morgan",
    "Murphy",
    "Navy",
    "Noel",
    "Oakley",
    "Ollie",
    "Onyx",
    "Paget",
    "Palmer",
    "Park",
    "Pat",
    "Peyton",
    "Phoenix",
    "Poe",
    "Presley",
    "Rain",
    "Raleigh",
    "Randy",
    "Reagan",
    "Reef",
    "Reese",
    "Remy",
    "Rene",
    "Ricky",
    "Ridley",
    "Ripley",
    "River",
    "Robbie",
    "Robin",
    "Rory",
    "Ross",
    "Rumi",
    "Sage",
    "Sailor",
    "Salem",
    "Sammie",
    "Sandy",
    "Sasha",
    "Scout",
    "Seneca",
    "Seven",
    "Shannon",
    "Shawn",
    "Shea",
    "Shelby",
    "Shiloh",
    "Sidney",
    "Sloan",
    "Spencer",
    "Stacy",
    "Story",
    "Sutton",
    "Tanner",
    "Taran",
    "Tatum",
    "Taylor",
    "Teagan",
    "Terry",
    "Tommie",
    "Tracy",
    "True",
    "Vesper",
    "Waverly",
    "West",
    "Wren",
    "Xenith",
    "Zephyr",
    "Zen",
    "Zion",
    "Zuri"
]

FULL_NAME_INPUT: Final[str] = (
    "You respond, \"actually, my name is...\"\n(Please enter "
    "First, Middle, and Last name): "
)

FULL_NAME_RE: Final[re.Pattern[str]] = re.compile(
    rf"""
    ^                   # Start anchor.
    (?!.*/s{2})          # Two space not allowed anywhere.
    [A-Z]               # Initial capitalization .
    [a-zA-Z'-]+        # Acceptable characters .
    (?:                 # Option to use the () enclosed tokens.
        [ ]             # Exactly one literal space
        [A-Z]           # Initial capitalization. (ONE Explicit space before)
        [a-zA-Z'-]+    # Acceptable characters
    ){{2}}                  # Previous token quantifier two more times.
    $                   # End anchor.
    """,
    re.VERBOSE
)

FULL_NAME_ERROR: Final[str] = (
    "First, Middle, and Last name are all required. First letter of names "
    "must be\ncapitalized. Only letters, and apostrophes (')\n"
    "and hyphens (-) are accepted.\n"
    "\"Don't give Guss no guff! Get going Gordon!!!\""
)

# ====================
# Message functions
# ====================
def guss_gusser_message(full_name: str) -> str:
    initials = get_initials(full_name)
    message = (
        f"{'*'*79}\nYou are not even sure he heard you as he brings his "
        "fingers to his temples.\nHe furrows his brow in concentration and "
        "ostentatiously orates,\n\"Ah your initials must be "
        f"{initials.strip()}!!!\"\nStunned, you nod numbly and drive away "
        "oblivious that the fueling hadn't\nfinished. \"GAH!\" Guss gasps as "
        "the nozzle pops out, drops, and sparks,\nblowing up the pump. You "
        "snap back to reality and realize that\n"
        "both you and Guss got...gas-lit."
    )
    return message

# ====================
# Logic Functions
# ====================
def build_full_name_guess() -> str:
    """
    Takes the global named constant lists of FIRST_NAMES and LAST_NAMES
    builds a full name guess from them.

    Returns
    -------
    full_name_guess: str
        First name, middle, and last name formatted.

    """
    first_name = FIRST_NAMES[randint(0, len(FIRST_NAMES) - 1)]
    middle_name = FIRST_NAMES[randint(0, len(FIRST_NAMES) - 1)]
    last_name =LAST_NAMES [randint(0, len(LAST_NAMES) - 1)]
    full_name_guess = f"\"{first_name} {middle_name} {last_name}. right?\""
    return full_name_guess


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


def get_initials(full_name: str) -> str:
    """
    Takes in a string of First, Middle, Last name and returnd the initials

    Parameters
    ----------
    full_name: str
        String of first, middle, last name.

    Returns
    -------
    initials: str
        Formatted initials string.

    """
    separated_names = full_name.split()
    initials_list = [name[0].upper() + "." for name in separated_names]
    initials = " ".join(initials_list)
    return initials


def main() -> None:
    print(INTRODUCTION_MESSAGE)
    print(build_full_name_guess())
    full_name = get_data(FULL_NAME_INPUT, FULL_NAME_RE, FULL_NAME_ERROR)
    print(guss_gusser_message(full_name))


if __name__ == "__main__":
    main()
