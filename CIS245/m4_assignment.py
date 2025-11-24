# CIS245-T303 Introduction to Programming
# Instructor: Dr. Sasan Azazian
# M4: Assignment - Functions
# Author: Eric J Turman
# Date: 10-04-2025
# email: ejturman@my365.bellevue.edu

from typing import Final

# ====================
# Named Constants
# ====================
KILOMETERS_PER_MILE: Final[float] = 1.60934

KILOM_EATER: str = "'Kilom-eater'"

GREETING_MESSAGE: str = (
    "~ \"Hi there!,\" giving you the Vulcan salute, "
    f"\"I'm {KILOM_EATER}.\"\n~ He thrusts his hand out grasping yours, "
    "pasta juice squelching as he\n~ grips your hand and shakes it too "
    "enthusiastically for far too long.\n~ You withdraw your hand and "
    "discretely wipe it on your pants.\n~ \"The Kilom pasta company makes "
    f"the tastiest noodles that are many miles long.\n~ {KILOM_EATER} leans "
    "in conspiratorially and whispers,\n~ \"but I convert the noodles from "
    f"miles to kilometers at a rate of\n~ {KILOMETERS_PER_MILE} per mile so "
    "I can have more to eat,\" winking.\n~ You look at him funny and are "
    "about to tell him that conversion doesn't work\n~ that way. But, before "
    "you can say anything, he hands you the keys to his car.\n~ " 
    "\"I filled the trunk with one noodle and,\" with a crazed look in his "
    "eyes,\n~ \"I will run behind you and eat it all up. When I finish the "
    "trunk-pasta\n~ tell me how many miles you drove. Then I will tell you "
    "how many\n~ kilometers of pasta I ate,\" laughing maniacally.\n~ "
    f"As you raise your finger to protest, {KILOM_EATER} opens his maw and\n~ "
    "runs at you doing his impression of Pac-Man! You hastily reach into "
    "the trunk\n~ and toss the end of the Kilom noodle into his mouth.\n~ "
    "Hurriedly you slip into the car. "
    "Better start driving or you are done-for!"
)

HOW_MANY_MILES_ASK: str = (
    "How many miles "
    "do you drive before \"Kilom-eater\" finishes the "
    "trunk-pasta? "
)

NEGATIVE_MESSAGE: str = (
    f"ৎ౨ You shift it into reverse, but {KILOM_EATER} dodges you and jumps\n"
    "ৎ౨ on the hood riding along with you. Try something else.\n"
)

STATIONARY_MESSAGE: str = (
    f"ৎ౨ Frozen in terror, you flinch as {KILOM_EATER} gnashes his teeth and "
    "pounds\nৎ౨ on the car door. You had better get moving before he breaks "
    "the window.\n"
)

AGAIN_ASK: str = "Are you up for another drive?"

AGAIN_INPUT: str = "('y', 'yes', 'n', 'no'): "

AGAIN_Y_MESSAGE: str = (
    f"\"Yay!\" {KILOM_EATER} loads the trunk with another Kilom noodle.\n"
    "\"Trunk-pasta, is locked and loaded!\" sticks one end of the noodle "
    "into his\nmouth and resumes his impression of Pac-Man.\n"
)

AGAIN_N_MESSAGE: str = (
    f"\"Aww! Thanks anyways\" {KILOM_EATER} waves goodbye\nand sings a song "
    f"to the tune of:\n'I wish I were an Oscar Meyer wiener.'\n"
    "\"♫♩ I wish I were a miles long Kilom noodle ♫♩\"\n"
    "\"♫♩ not some other kind of food that's junk. ♫♩\"\n"
    "\"♫♩ And if I were a miles long Kilom noodle ♫♩\"\n"
    "\"♫♩ somebody could eat me from their trunk. ♫♩\"\n"
)

# ====================
# Message Functions
# To keep using f-string and avoid .format
# ====================
def exception_message(exception_type, input_miles) -> str:
    """
    Build exception message

    Parameters
    ----------
    exception_type
    input_miles

    Returns
    -------
    output_message: str
        Concatenated string
    """
    output_message = (
        f"{KILOM_EATER} shakes his head and with the noodle dangling "
        "from his lips says,\n"
        "\"Please! This is serious-spaghetti not pretend-pasta! End your "
        "distance denial.\n"
        f"How can I put this delicately? I {exception_type}\"\n"
        "Glaring at you as you say nothing he blurts out, "
        f"\"'{input_miles}' is nonsense!\n"
        "Enter a number, please!\"\n"
    )
    return output_message


def distance_message(input_miles: float, input_kilometers: float) -> str:
    """
    Builds distance driven message

    Parameters
    ----------
    input_miles: float
    input_kilometers: float

    Returns
    -------
    output_message: str
        Concatenated string
    """
    miles: str = str()
    test_miles: int = int(input_miles)
    if test_miles == input_miles:
        miles = "mile"
    else:
        miles = "miles"

    kilometers: str = str()
    test_kilometers: int = int(input_kilometers)
    if test_kilometers == input_kilometers:
        kilometers = "kilometer"
    else:
        kilometers = "kilometers"

    output_message: str = (
        f"{KILOM_EATER} pats his belly and, belching, says, \"that was "
        f"delicious!\n"
        f"You drove {input_miles} {miles} and I ate a Kilom noodle that was\n"
        f"{input_kilometers:.5f} {kilometers} long!\"\n"
    )
    return output_message


def again_other_message(input_message: str) -> str:
    """
    Builds message for input not matching y/yes/n/no

    Parameters
    ----------
    input_message

    Returns
    -------
    output_message: str
        Concatenated string
    """
    output_message: str = (
        f"*snif* Tears well up in {KILOM_EATER}'s eyes \"You could be honest "
        "with me\nInstead of pretending to speak another language.\"\n"
        f"{KILOM_EATER} glares at you. \"You are im-past-able to "
        "understand!\"\n"
        f"\"What does '{input_message}' even mean?! I'll take it as "
        "a 'no'.\"\nTurns and walks away, shoulders slumped."
    )
    return output_message

# ====================
# Logic Functions
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
        case "~" | "౨ৎ":
            print(
                f"{fill_char * fill_length}\n"
                f"{message}\n"
                f"{fill_char * fill_length}\n"
            )
        case "(ಠ_ಠ)" | "waka " | ".":
            print(
                f"{'-' * 79}\n"
                f"{fill_char * fill_length}\n"
                f"{message}"
            )
        case _:
            print(f"౨ৎ {message} ৎ౨")


def get_miles() -> float:
    """
    Prompts a valid input and returns a float representing miles driven.

    Returns
    -------
    float_miles: float
        The distance in miles.
    """
    while True:
        input_miles = input(HOW_MANY_MILES_ASK)
        try:
            float_miles = float(input_miles)
            if float_miles < 0:
                format_message(NEGATIVE_MESSAGE, "(ಠ_ಠ)", 14)
                continue
            elif float_miles == 0:
                format_message(STATIONARY_MESSAGE, "(ಠ_ಠ)", 14)
                continue
            # Early return
            return float_miles
        except ValueError as exception_type:
            format_message(
                exception_message(exception_type, input_miles),
                "(ಠ_ಠ)",
                14
            )
    raise RuntimeError("Unreachable: get_mile loop exited unexpectedly")


def miles_to_kilometers(miles: float) -> float:
    """
    Convert miles to kilometers.

    Parameters
    ----------
    miles : float
        Distance in miles.

    Returns
    -------
    kilometers_from_miles: float
        Equivalent distance in kilometers.
    """
    kilometers_from_miles: float = miles * KILOMETERS_PER_MILE
    return kilometers_from_miles


def again() -> bool:
    """
    Asks user if they want to go again and displays appropriate story message

    Returns
    -------
        True or False Boolean
    """
    format_message(AGAIN_ASK)
    go_again = input(AGAIN_INPUT).strip().lower()
    match go_again:
        case "y" | "yes":
            format_message(AGAIN_Y_MESSAGE, ".")
            return True
        case "n" | "no":
            format_message(AGAIN_N_MESSAGE, ".")
        case _:
            format_message(again_other_message(go_again), ".")
    return False


def main() -> None:
    """
    Main Program loop
    """
    format_message(GREETING_MESSAGE, "~")
    drive = True
    while drive == True:
        miles = get_miles()
        kilometers = miles_to_kilometers(miles)
        format_message(
            distance_message(miles, kilometers),
            "waka ",
            15
        )
        drive = again()


if __name__ == '__main__':
    main()
