"""
CIS245-T303 Introduction to Programming
Instructor: Dr. Sasan Azazian
Assignment: M6 – Python List Program
Author: Eric J. Turman
Date: 2025-10-18
Email: ejturman@my365.bellevue.edu

The assignment is for a program that prompts the user for a series of
20 numbers. Then, the program should store the numbers in a list and
display the following data:
* The lowest number in the list.
* The highest number in the list.
* The total of the numbers in the list.
* The average of the numbers in the list.

To elevate the assignment, the narrative of a fictitious sport of "ro-bat-ball"
is used to allow for number at bat that far exceed human capabilities. This is
for the purpose of having a large number range. Additionally, the potential
times at bat will be pulled randomly.

The program is left open for to modify of more or fewer games in a season.

"""
from random import randint
from typing import (
    Final,
    Literal
)

# ====================
# Named Constants
# ====================

MIN_PITCHES: Final[int] = 30
MAX_PITCHES: Final[int] = 999
SEASON_LENGTH: Final[int] = 20

INTRO_MESSAGE: str = (
    f"{'+'*79}\nWelcome to 'Ro-Bat-Ball.' You played a good series of "
    f"{SEASON_LENGTH} games.\nNow it time to tally your scores. You'll be "
    f"honest, right?\n{'+'*79}"
)


# ====================
# Message functions
# ====================

def hits_input_message(
        game: int,
        at_bats: int
) -> str:
    """
    Concatenates the input message using f-strings

    Parameters
    ----------
    game: int
        Current game number in the series to let the user know how far through
        the input process they are.

    at_bats: int
        The current game's number of pitches that wer at bats

    Returns
    -------
    input_message: str
        Concatenated input message

    """
    input_message = (
        f"In game #{game + 1}, the ro-pitcher threw {at_bats} pitches "
        "to you.\nEnter how many of the pitches you hit: "
    )
    return input_message


def hits_error_message(
        at_bats: int,
        raw_hits: str,
        mode: Literal["value", "negative", "over"]

) -> str:
    """
    Concatenates all the input error messages to return a appropriate string

    Parameters
    ----------
    at_bats: int
        The current game's number of pitches that wer at bats

    raw_hits

    mode

    Returns
    -------

    """
    base_message = (
        f"Invalid input: Only whole numbers between 0 and {at_bats} "
        f"allowed.\n"
    )

    match mode:
        case "value":
            error_message = (
                f"{base_message}*bzzzt* {raw_hits} does not compute! "
                 f"<crackle>"
            )
        case "negative":
            error_message = (
                f"{base_message}{raw_hits} hits?!? Even you are not that "
                f"bad. Try again, please."
            )
        case "over":
            error_message = (
                f"{base_message}I wasn't born yesterday. What pseudo-math are "
                f"you trying to pull on me?\nHow can you hit {raw_hits} "
                f"when there were only {at_bats} thrown?"
            )
        case _:
            raise ValueError(f"Invalid mode: {mode}")

    return error_message



# ====================
# Logic functions
# ====================

def get_valid_hits(game: int, at_bats: int) -> int:
    """
    Asks for valid user input an number of hits they as a robo-batter hit.
    in order to be valid it need to be zero or grater and less than or equal
    to the number of at bats pitched to them

    Parameters
    ----------
    game: int
        Current game number in the series to let the user know how far through
        the input process they are.

    at_bats: int
        The current game's number of pitches that wer at bats

    Returns
    -------
    int_hits: int
        The validated input value that the user entered for hits

    """

    while True:
        raw_hits = input(hits_input_message(game, at_bats))
        try:
            int_hits = int(raw_hits)
            if int_hits > at_bats:
                error_details = hits_error_message(
                    at_bats,
                    raw_hits,
                    "over"
                )
                print(
                    f"{'!' * 79}\n{error_details}\n{'!' * 79}\n"
                )
            elif int_hits < 0:
                error_details = hits_error_message(
                    at_bats,
                    raw_hits,
                    "negative"
                )
                print(
                    f"{'!' * 79}\n{error_details}\n{'!' * 79}\n"
                )
            else:
                return int_hits

        except ValueError as error:
            error_details = hits_error_message(
                at_bats,
                raw_hits,
                "value"
            )
            print(
                f"{'!'*79}\n{error}\n{error_details}\n{'!'*79}\n"
            )


def build_game_series(
        mode: Literal["manual", "auto"] = "manual",
        number_of_games: int = SEASON_LENGTH
) -> list[tuple[int, int]]:
    """
    Builds up the information for pitches that count as at bats and
    hits for the entire sseries of games. sotring them in a list of tupes of
    integer pairs where index 0 represents the at bats and index 1 is the
    number of hits. Hooks for automatic mode.
    TODO: add automatic mode in the future

    Parameters
    ----------
    mode: str
        Set the program run mode. may only be manual or automatic
    number_of_games: int
        The number of the tuple string pairs


    Returns
    -------

    """
    games: list[tuple[int, int]] = []

    for game in range(number_of_games):
        at_bats = randint (MIN_PITCHES, MAX_PITCHES)
        match mode:
            case "manual":
                hits = get_valid_hits(game, at_bats)
            case _:
                hits = 0
        games.append((at_bats, hits))
    return games


def get_list(
        game_series: list[tuple[int, int]],
        mode: Literal["at_bats", "hits"]
) -> list[int]:
    """
    Takes the game series raw information and compiles them into lists for
    either at bats or hits based on the mode

    Parameters
    ----------
    game_series: list[tuple[int, int]
        The data structure representing the all information for all the games
    mode: Literal["at_bats", "hits"]
        Changes what list values are extracted (at bats or hits)
    Returns: list[int]
        Either returns the list of at bats or hits or None

    -------
    a list of integers for at bats of hits

    """
    number_list: list[int] = []
    match mode:
        case "at_bats":
            return [game[0] for game in game_series]
        case "hits":
            return [game[1] for game in game_series]
        case _:
            raise ValueError(f"Invalid mode: {mode}")


def process_games(
        at_bats: list[int],
        hits: list[int],
        mode: Literal["min", "max", "sum", "average", "bat_average"]
) -> None:
    """
    Takes an input list and processes it for min, max, total, average. and
    batting average based on input mode

    Parameters
    ----------
    at_bats: list[str]
        How many robo-pitches that counted toward the players batting average
    hits: list[str]
        How many hits the robo-player made off of the available at bats
    mode: Literal ["min", "max", "sum", "average"] default "average"
        How the function th input list data
    """

    match mode:
        case "min":
            min_hits = min(hits)
            print(f"Your lowest number of hits was: {min_hits}")
        case "max":
            max_hits = max(hits)
            print(f"Your highest number of hits was: {max_hits}")
        case "sum":
            total_hits = sum(hits)
            print(f"Your total hits for the series were: {total_hits}")
        case "average":
            average_hits = sum(hits) / SEASON_LENGTH
            print(f"Your average hits were: {average_hits:.1f} per game")
        case "bat_average":
            batting_average = sum(hits) / sum(at_bats)
            print(f"Your batting average is: {batting_average:.3f}")
        case _:
            raise ValueError(f"Invalid mode: {mode}")

    return None


def main() -> None:
    """
    Main program loop calls to build the game information
    pulls lists of at bats and hits
    calls to process and display the results

    """
    print(INTRO_MESSAGE)
    game_series = build_game_series()
    at_bats_list = get_list(game_series, "at_bats")
    hits_list = get_list(game_series, "hits")
    print(f"{'='*79}\n")
    process_games(at_bats_list, hits_list, "min")
    process_games(at_bats_list, hits_list, "max")
    process_games(at_bats_list, hits_list, "sum")
    process_games(at_bats_list, hits_list, "average")
    process_games(at_bats_list, hits_list, "bat_average")

if __name__ == "__main__":
    main()
