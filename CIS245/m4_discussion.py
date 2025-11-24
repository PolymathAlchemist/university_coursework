# CIS245-T303 Introduction to Programming
# Instructor: Dr. Sasan Azazian
# M4: Discussion Board - Functions
# Author: Eric J Turman
# Date: 09-30-2025
# email: ejturman@my365.bellevue.edu

from typing import Final

# ====================
# Named Constants
# ====================
LITERS_PER_GALLON: Final[float] = 3.78541

INTRO_MESSAGE: str = (
    "+ Behold! For I am \"Gallon-tron\"! <booming voice echoes in your head>\n"
    "+ Give unto me your watery gallons and "
    "Witness them magically multiply!!!\n+ Transforming every gallon "
    f"at an astounding rate of {LITERS_PER_GALLON} liters per gallon!"
)
HOW_MANY_GALLONS: str = "How many gallons will you give to Gallon-tron? "

HYDRATION_MESSAGE: str = (
    "\n(っ◔◡◔)っ⋆˖⁺‧ I, \"Gallon-tron\" will now employ my "
    "powers of HYDRATION HYPE!"
)

MAGIC_MESSAGE: str = (
    "*༺✩˚POOF!✩༻*₊ your original {gallons} gallons has become "
    "{liters:.5f} liters!"
)
TRY_AGAIN: str = (
    "Dost thou wish to witness more Numeric Ninja-nanegans? (y/n) "
)

SOMETHING_FOR_NOTHING_MESSAGE: str = (
    "♫♩ To roughly quote the Canadian rock band Rush:\n"
    "♫♩ \"You can't get somethin' for nothin'! You can't get [liters] for "
    "free!\""
)

NEGATIVE_MESSAGE: str = "Really?! (ಠ_ಠ) Don't be so negative."

ONE_MORE_TIME_MESSAGE: str = (
    "♫♩ The song \"One More Time\" by Daft Punk starts "
    "playing suddenly from nowhere!"
)

EXCEPTION_MESSAGE: str = (
    "{exception_type}\nCan you not read?! \"{input_gallons}\" is not a number."
    "\n\"Gallon-tron\" only accepts numbers. Try harder!\n"
)

EXIT_MESSAGE: str = (
    "As the mighty spectre of Gallon-tron fades, your pet dog \"Ruh-roh\" "
    "pulls back a\ncurtain revealing that Gallon-tron is actually the "
    "American musician Beck with:\n'Two calculators and a microphone'"
)

# ====================
# Functions
# This program is using NumPy-style docstrings
# ====================
def format_message(
        message: str,
        fill_char: str ="",
        fill_length: int = 79
) -> None:
    """
    Display formatted messages based on the fill character, if provided.

    Parameters
    ----------
    message : str
        The message string to format and print.
    fill_char : str, optional
        Character to use as border decoration (default is an empty string).
    fill_length : int, optional
        How many times to repeat the fill_char (default is 79).
    """
    match fill_char:
        case "+" | "♫♩":
            print(
                f"{fill_char * fill_length}\n"
                f"{message}\n"
                f"{fill_char * fill_length}\n"
            )
        case "!" | "=" | ".":
            print(
                f"{fill_char * fill_length}\n"
                f"{message}"
            )
        case _:
            print(f"-=[ {message} ]=-")


def get_gallons() -> float:
    """
    Prompts a valid input and returns a float representing the gallons.

    Returns
    -------
    float
        The gallons amount.

    """
    while True:
        input_gallons = input(HOW_MANY_GALLONS)
        try:
            float_gallons = float(input_gallons)
            if float_gallons < 0:
                format_message(NEGATIVE_MESSAGE)
                continue
            elif float_gallons == 0:
                format_message(SOMETHING_FOR_NOTHING_MESSAGE, "♫♩", 39)
                continue
            # Early return
            return float_gallons
        except ValueError as exception_type:
            format_message(
                EXCEPTION_MESSAGE.format(
                    exception_type=exception_type,
                    input_gallons=input_gallons),
                "!",
                33
            )
    raise RuntimeError("Unreachable: get_gallons loop exited unexpectedly")


def gallons_to_liters(gallons: float) -> float:
    """
    Convert gallons to liters.

    Parameters
    ----------
    gallons : float
        Measurement in U.S. gallons

    Returns
    -------
    liters_from_gallons: float
        Equivalent measurement in liters
    """
    liters_from_gallons = gallons * LITERS_PER_GALLON
    return liters_from_gallons


def main() -> None:
    """
    Run the main program loop
    Displays an intro message and prompts the user to input number of
    gallons; retrying if the input is invalid.
    Outputs a message of the equivalent liters.
    """
    format_message(INTRO_MESSAGE, "+")
    again = "y"

    while again == "y":
        gallons = get_gallons()
        liters = gallons_to_liters(gallons)
        format_message(HYDRATION_MESSAGE, "=")
        format_message(MAGIC_MESSAGE.format(gallons=gallons, liters=liters))
        again = input(TRY_AGAIN)
        again = again.lower()
        if again == "y":
            format_message(ONE_MORE_TIME_MESSAGE, "♫♩", 39)

    format_message(EXIT_MESSAGE, ".")


# Call the main function only if the file is executed directly
if __name__ == "__main__":
    main()
