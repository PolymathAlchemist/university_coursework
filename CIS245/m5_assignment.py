"""
CIS245-T303 Introduction to Programming
Instructor: Dr. Sasan Azazian
Assignment: M5 – Python File Processing Program
Author: Eric J. Turman
Date: 2025-09-30
Email: ejturman@my365.bellevue.edu

This program prompts the user for a file name, full name, street address,
and phone number. Comma-separated values (CSV) were used to write the data to
the file and then read back to confirm successful file I/O.

The program emphasizes robust input validation using regular expressions,
modular design with reusable functions, and consistent documentation practices.
It employs selected data types from future chapters
(e.g., lists, tuples, and sets) as well as uncovered techniques
(e.g., type hints, regular expressions, and the CSV module)
to achieve the input validation that was emphasized.

Data Source
-----------
Street suffix abbreviations are derived directly from the official USPS
Street Abbreviations Job Aid, compiled from:
https://studyinthestates.dhs.gov/sites/default/files/USPS%20Street%20Abbreviations%20Job%20Aid.pdf
Using Microsoft Excel. Duplicates purposely left in for demonstration.
"""

import re
from typing import Final
import csv

# ====================
# Named Constants
# ====================

# One address suffix set per line in case expansion is wanted.
SUFFIX_GROUPS: Final[list[tuple[str, str]]] = [
    ("Alley", "ALY"),
    ("Annex", "ANX"),
    ("Apartment", "APT"),
    ("Arcade", "ARC"),
    ("Avenue", "AVE"),
    ("Basement", "BSMT"),
    ("Bayou", "BYU"),
    ("Beach", "BCH"),
    ("Bend", "BND"),
    ("Bluff", "BLF"),
    ("Bluffs", "BLFS"),
    ("Bottom", "BTM"),
    ("Boulevard", "BLVD"),
    ("Branch", "BR"),
    ("Bridge", "BRG"),
    ("Brook", "BRK"),
    ("Brooks", "BRKS"),
    ("Building", "BLDG"),
    ("Burg", "BG"),
    ("Burgs", "BGS"),
    ("Bypass", "BYP"),
    ("Camp", "CP"),
    ("Canyon", "CYN"),
    ("Cape", "CPE"),
    ("Causeway", "CSWY"),
    ("Center", "CTR"),
    ("Centers", "CTRS"),
    ("Circle", "CIR"),
    ("Circles", "CIRS"),
    ("Cliff", "CLF"),
    ("Cliffs", "CLFS"),
    ("Club", "CLB"),
    ("Common", "CMN"),
    ("Corner", "COR"),
    ("Corners", "CORS"),
    ("Course", "CRSE"),
    ("Court", "CT"),
    ("Courts", "CTS"),
    ("Cove", "CV"),
    ("Coves", "CVS"),
    ("Creek", "CRK"),
    ("Crescent", "CRES"),
    ("Crest", "CRST"),
    ("Crossing", "XING"),
    ("Crossroad", "XRD"),
    ("Curve", "CURV"),
    ("Dale", "DL"),
    ("Dam", "DM"),
    ("Department", "DEPT"),
    ("Divide", "DV"),
    ("Drive", "DR"),
    ("Drives", "DRS"),
    ("Estate", "EST"),
    ("Estates", "ESTS"),
    ("Expressway", "EXPY"),
    ("Extension", "EXT"),
    ("Extensions", "EXTS"),
    ("Fall", "FALL"),
    ("Falls", "FLS"),
    ("Ferry", "FRY"),
    ("Field", "FLD"),
    ("Fields", "FLDS"),
    ("Flat", "FLT"),
    ("Flats", "FLTS"),
    ("Floor", "FL"),
    ("Ford", "FRD"),
    ("Fords", "FRDS"),
    ("Forest", "FRST"),
    ("Forge", "FRG"),
    ("Forges", "FRGS"),
    ("Fork", "FRK"),
    ("Forks", "FRKS"),
    ("Fort", "FT"),
    ("Freeway", "FWY"),
    ("Front", "FRNT"),
    ("Garden", "GDN"),
    ("Gardens", "GDNS"),
    ("Gateway", "GTWY"),
    ("Glen", "GLN"),
    ("Glens", "GLNS"),
    ("Green", "GRN"),
    ("Greens", "GRNS"),
    ("Grove", "GRV"),
    ("Groves", "GRVS"),
    ("Hangar", "HNGR"),
    ("Harbor", "HBR"),
    ("Harbors", "HBRS"),
    ("Haven", "HVN"),
    ("Heights", "HTS"),
    ("Highway", "HWY"),
    ("Hill", "HL"),
    ("Hills", "HLS"),
    ("Hollow", "HOLW"),
    ("Inlet", "INLT"),
    ("Island", "IS"),
    ("Islands", "ISS"),
    ("Isle", "ISLE"),
    ("Junction", "JCT"),
    ("Junctions", "JCTS"),
    ("Key", "KY"),
    ("Keys", "KYS"),
    ("Knoll", "KNL"),
    ("Knolls", "KNLS"),
    ("Lake", "LK"),
    ("Lakes", "LKS"),
    ("Land", "LAND"),
    ("Landing", "LNDG"),
    ("Lane", "LN"),
    ("Light", "LGT"),
    ("Lights", "LGTS"),
    ("Loaf", "LF"),
    ("Lobby", "LBBY"),
    ("Lock", "LCK"),
    ("Locks", "LCKS"),
    ("Lodge", "LDG"),
    ("Loop", "LOOP"),
    ("Lot", "LOT"),
    ("Lower", "LOWR"),
    ("Mall", "MALL"),
    ("Manor", "MNR"),
    ("Manors", "MNRS"),
    ("Meadow", "MDW"),
    ("Meadows", "MDWS"),
    ("Mews", "MEWS"),
    ("Mill", "ML"),
    ("Mills", "MLS"),
    ("Mission", "MSN"),
    ("Motorway", "MTWY"),
    ("Mount", "MT"),
    ("Mountain", "MTN"),
    ("Mountains", "MTNS"),
    ("Neck", "NCK"),
    ("Office", "OFC"),
    ("Orchard", "ORCH"),
    ("Oval", "OVAL"),
    ("Overpass", "OPAS"),
    ("Park", "PARK"),
    ("Park", "PARK"),
    ("Parkway", "PKWY"),
    ("Parkways", "PKWY"),
    ("Pass", "PASS"),
    ("Passage", "PSGE"),
    ("Path", "PATH"),
    ("Penthouse", "PH"),
    ("Pier", "PIER"),
    ("Pike", "PIKE"),
    ("Pine", "PNE"),
    ("Pines", "PNES"),
    ("Place", "PL"),
    ("Plain", "PLN"),
    ("Plains", "PLNS"),
    ("Plaza", "PLZ"),
    ("Point", "PT"),
    ("Points", "PTS"),
    ("Port", "PRT"),
    ("Prairie", "PR"),
    ("Radial", "RADL"),
    ("Ramp", "RAMP"),
    ("Ranch", "RNCH"),
    ("Rapid", "RPD"),
    ("Rapids", "RPDS"),
    ("Rear", "REAR"),
    ("Rest", "RST"),
    ("Ridge", "RDG"),
    ("Ridges", "RDGS"),
    ("River", "RIV"),
    ("Road", "RD"),
    ("Roads", "RDS"),
    ("Route", "RTE"),
    ("Row", "ROW"),
    ("Rue", "RUE"),
    ("Run", "RUN"),
    ("Shoal", "SHL"),
    ("Shoals", "SHLS"),
    ("Shore", "SHR"),
    ("Shores", "SHRS"),
    ("Side", "SIDE"),
    ("Skyway", "SKWY"),
    ("Slip", "SLIP"),
    ("Space", "SPC"),
    ("Spring", "SPG"),
    ("Springs", "SPGS"),
    ("Spur", "SPUR"),
    ("Spurs", "SPUR"),
    ("Square", "SQ"),
    ("Squares", "SQS"),
    ("Station", "STA"),
    ("Stop", "STOP"),
    ("Stravenue", "STRA"),
    ("Stream", "STRM"),
    ("Street", "ST"),
    ("Streets", "STS"),
    ("Suite", "STE"),
    ("Summit", "SMT"),
    ("Terrace", "TER"),
    ("Throughway", "TRWY"),
    ("Trace", "TRCE"),
    ("Track", "TRAK"),
    ("Trafficway", "TRFY"),
    ("Trail", "TRL"),
    ("Trailer", "TRLR"),
    ("Tunnel", "TUNL"),
    ("Turnpike", "TPKE"),
    ("Underpass", "UPAS"),
    ("Union", "UN"),
    ("Unions", "UNS"),
    ("Unit", "UNIT"),
    ("Upper", "UPPR"),
    ("Valley", "VLY"),
    ("Valleys", "VLYS"),
    ("Viaduct", "VIA"),
    ("View", "VW"),
    ("Views", "VWS"),
    ("Village", "VLG"),
    ("Villages", "VLGS"),
    ("Ville", "VL"),
    ("Vista", "VIS"),
    ("Vista", "VIS"),
    ("Walk", "WALK"),
    ("Walks", "WALK"),
    ("Wall", "WALL"),
    ("Way", "WAY"),
    ("Ways", "WAYS"),
    ("Well", "WL"),
    ("Wells", "WLS")
]

# Collapse SUFFIX_GROUPS into a set, removing any potential duplicates.
SUFFIX_SET: Final[set[str]] = {
    suffix for suffix_group in SUFFIX_GROUPS for suffix in suffix_group
}

# Turn the set into a sorted list with longer street suffixes first so that
# a match is not automatically made by St when Street is misspelled as Streat.
SUFFIX_SORTED: Final[list[str]] = sorted(
    SUFFIX_SET,
    key = len,
    reverse = True
)

# Combine into a long string that re.compile can use to validate input.
SUFFIXES: Final[str] = "|".join(SUFFIX_SORTED)

ADDRESS_INPUT: Final[str] = "Please enter your street address: "

# Builds the regex matching pattern
# Using https://regex101.com/ to help figure out the pattern and test.
# Inline comments to break down each step of what each part is matching.
ADDRESS_RE: Final[re.Pattern[str]] = re.compile(
    rf"""
        ^                   # Start anchor.
        (?!.*[ ]{{2}})      # Forbids two consecutive spaces.
        \d{{1,6}}           # House number (1–6 digits).
        \s+                 # At least one space.
        [A-Za-z0-9.'-]+     # First street token (e.g., N., 5th, Main).
        (?:
            [ ]             # Only one space.
            [A-Za-z0-9.'-]+ # Acceptable Characters.
        )*                  # Zero or more MORE tokens.
        \s+                 # At least one space before suffix.
        (?:{SUFFIXES})      # Suffix alts (e.g., St|Street|Ave|Avenue...).
        \.?                 # Optional trailing period.
        $                   # End anchor.
        """,
    re.IGNORECASE | re.VERBOSE
)

ADDRESS_ERROR: Final[str] = (
    "Only a valid street address format is accepted. Example:\n"
    "123 North Street -or- 123 N. St. NO CITY, STATE, OR ZIP, please!"
)

PHONE_NUMBER_INPUT: Final[str] = (
    "Please enter the phone number with area code: "
)

PHONE_NUMBER_RE: re.Pattern[str] = re.compile(
    r"""
    ^                   # Start anchor.
    (?:\(\d{3}\)|\d{3}) # 3 digit Area code with or without () around it.
    [\s.-]?             # Optional separator.
    \d{3}               # 3 digits.
    [\s.-]?             # Optional separator.
    \d{4}               # 4 digits.
    $                   # End anchor.
    """,
    re.VERBOSE          # Allow for breaking up into multi-line for clarity.
)

PHONE_NUMBER_ERROR: Final[str] = (
    "Only a valid phone number with area code is accepted. Example\n"
    "123.456.7890 -or- (123) 456-7890 -or- 123 456 7890, please!"
)

FULL_NAME_INPUT: Final[str] = (
    "Please enter the full name.\n"
    "(At least first and last is required): "
)

FULL_NAME_RE: Final[re.Pattern[str]] = re.compile(
    rf"""
    ^                   # Start anchor.
    (?!.* {2})          # Two space not allowed anywhere.
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
    "Middle initials are Fine, but must be followed by a period."
)

FILE_NAME_INPUT: str = "Please enter filename: "

FILE_NAME_RE: Final[re.Pattern[str]] = re.compile(
    r"""
    ^                   # Start anchor.
    (?!\.\.)            # Not starting with two dots (e.g., "..name").
    (?!                 # Not a reserved DOS device name (even with extension).
        (?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])
        (?:\..*)?$
    )
    (?!\s)              # no leading space.
    (?!.*[<>:"/\\|?*\x00-\x1F]) # No invalid or control chars anywhere.
    (?!.*[ .]$)         # No trailing space or dot.
    .{1,100}            # Length between 1 and 100.
    $                   # End Anchor.
    """,
    re.IGNORECASE | re.VERBOSE    # Breaking up into multi-line for clarity.
)

FILE_NAME_ERROR: Final[str] = (
    "Illegal filename:\n"
    "    Can not start with two dots,"
    "    can not be named: con, prn, aux, nul com(1-9) or lpt(1-9),"
    "    can not have the extension: con, prn, aux, nul com(1-9) or lpt(1-9),"
    "    can not have a leading or tailing space,"
    "    can not have a trailing dot"
    "    can not be longer than 100 characters" # Mindful of full path length
)

# ====================
# Logic Functions
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
        Regular expression patter to filter for correct input
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


def get_record() -> list[str]:
    """
    Collect name, address, and phone number data to be used as a record.

    Returns
    -------
    record: list[str]
        Returns name, address and phone number in a string list record.
    """
    record: list[str] = []
    # Ask User for their valid full name.
    user_name = get_data(
        FULL_NAME_INPUT,
        FULL_NAME_RE,
        FULL_NAME_ERROR
    )
    record.append(user_name)
    # Ask user for their valid street address.
    street_address = get_data(
        ADDRESS_INPUT,
        ADDRESS_RE,
        ADDRESS_ERROR
    )
    record.append(street_address)
    # Ask user for a valid phone number.
    phone_number = get_data(
        PHONE_NUMBER_INPUT,
        PHONE_NUMBER_RE,
        PHONE_NUMBER_ERROR
    )
    record.append(phone_number)
    return record


def get_records_loop() -> list[list[str]]:
    """
    Collects each record and adds them into a list of records. Loops until
    user does not answer "y" or "yes" to adding another.

    Returns
    -------
    records: list[list[str]]
        Yields list of records.
    """
    records: list[list[str]] = []
    while True:
        records.append(get_record())
        again = input("Add another record? (y/yes/n/no): ").strip().lower()
        if again not in {"y", "yes"}:
            break
    return records


def file_csv_io(
        file_name: str,
        records: list[list[str]] | None = None,
        mode: str = "r",
        extended_mode: str = "",
        encoding: str = "utf-8"
) -> str | list[list[str]] | None:
    """
    Handles reading and writing of file i/o in csv format. Designed be
    repurposed and expanded for future programs to accommodate the other
    i/o modes. One nice feature for future expansion would to offer passing in
    a path object as an alternative to just the filename.

    Parameters
    ----------
    file_name: str
        Name of the save file.
    records: list[str] | None
        Accepts a list of strings
    mode: str
        Read/write mode:
            'a'     append to file
            'w'     overwrite file
            'r'     read file contents
    extended_mode: str
            'csv'  concatenate to mode to create 'rcsv' mode_match
    encoding: str
        Specifies encoding format. Dfault is 'utf-8'
    Returns
        Returns based on mode parameter:
            'a'&'w' returns None.
            'r'     returns file contents as a string.
            'rcsv'  returns file contents as a list of lists of strings.
    -------

    """
    with open(file_name, mode=mode, newline="", encoding=encoding) as file:
        mode_match = mode + extended_mode
        match mode_match:
            case "a" | "w":
                if records is None:
                    raise ValueError(
                        "Data must be provided when writing to a file."
                    )
                writer = csv.writer(file)
                writer.writerows(records)
                return None
            case "r":
                return file.read()
            case "rcsv":
                reader = csv.reader(file)
                return list(reader)
            case _:
                raise ValueError(
                    f"{'!'*79}\n{mode}{extended_mode} "
                    f"is unsupported as a mode "
                    f"(+ optional extended mode)\n"
                    f"{'!'*79}"
                )


def main() -> None:
    """
    Main program:
        asks user for file name, collects records,
        writes to fie file,
        displays what was written to the file,
        reads the file and displays the contents both as raw
            and csv.reader as a list for comparison.
    """

    # Ask user for a valid filename and append .csv if they do not.
    file_name = get_data(
        FILE_NAME_INPUT,
        FILE_NAME_RE,
        FILE_NAME_ERROR
    )
    if not file_name.lower().endswith(".csv"):
        file_name += ".csv"

    records = get_records_loop()

    file_csv_io(
        file_name,
        records,
        "w"
    )
    print(
        f"{'-'*79}\nRaw records written to {file_name}:\n{records}\n"
    )

    read_records = file_csv_io(
        file_name,
        mode="r"
    )
    print(f"{'='*79}\nRaw records read:\n{read_records}")

    read_records = file_csv_io(
        file_name,
        mode="r",
        extended_mode="csv"
    )
    print(f"{'='*79}\nCSV reader records read:\n{read_records}")


if "__main__" == __name__:
    main()
