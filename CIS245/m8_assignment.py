"""
CIS245-T303 Introduction to Programming
Instructor: Dr. Sasan Azazian
Assignment: M8 – Python Dictionary Program
Author: Eric J. Turman
Date: 2025-11-02
Email: ejturman@my365.bellevue.edu

This program prompts the user for a valid stock ticker symbol, If the input
matches one of the dictionary keys, display information about the stock.
If the user enters in a value that is not in the dictionary, it will respond
with an appropriate error message.

The program emphasizes robust input validation using regular expressions,
modular design with reusable functions, and consistent NumPy
documentation practices.

Data Sources
-----------
Names for this project were compiled from the following sources:
https://www.slickcharts.com/nasdaq100

Manually extracted Web information and formatted by with
Excel, and Sublime Text3.
"""

import re
import textwrap
from typing import (
    Final,
    Literal
)

# ====================
# Named Constants
# ====================

# {Stock symbol: (Name, Points, Point change, % change, Portfolio weight)}
STOCKS_DICT: Final[dict[str, tuple[str, float,float,float,float]]] = {
"NVDA": ("Nvidia", 202.49, -0.0020, -0.4, 0.1443),
"AAPL": ("Apple Inc.", 270.37, -0.0038, -1.03, 0.1169),
"MSFT": ("Microsoft", 517.81, -0.0151, -7.95, 0.1127),
"AMZN": ("Amazon", 244.22, -0.0958, 21.36, 0.0764),
"GOOGL": ("Alphabet Inc.", 281.19, -0.0010, -0.29, 0.0514),
"AVGO": ("Broadcom Inc.", 369.63, -0.0182, -6.84, 0.0511),
"GOOG": ("Alphabet Inc.", 281.82, -0.0003, -0.08, 0.0481),
"META": ("Meta Platforms", 648.35, -0.0272, -18.12, 0.0478),
"TSLA": ("Tesla, Inc.", 456.56, -0.0374, 16.46, 0.0444),
"PLTR": ("Palantir Technologies", 200.47, -0.0304, 5.92, 0.0139),
"NFLX": ("Netflix", 1118.86, -0.0274, 29.86, 0.0139),
"AMD": ("Advanced Micro Devices Inc.", 256.12, -0.0050, 1.28, 0.0122),
"ASML": ("ASML Holding", 1059.23, -0.0151, -16.22, 0.0120),
"COST": ("Costco", 911.45, -0.0095, -8.73, 0.0118),
"CSCO": ("Cisco", 73.11, -0.0027, 0.2, 0.0084),
"AZN": ("AstraZeneca", 82.4, -0.0007, 0.06, 0.0075),
"MU": ("Micron Technology", 223.77, -0.0011, -0.24, 0.0074),
"TMUS": ("T-Mobile US", 210.05, -0.0028, -0.6, 0.0069),
"SHOP": ("Shopify", 173.86, -0.0014, 0.25, 0.0066),
"APP": ("Applovin Corp", 637.33, -0.0269, 16.71, 0.0063),
"PEP": ("PepsiCo", 146.09, -0.0099, -1.46, 0.0058),
"LRCX": ("Lam Research", 157.46, -0.0220, -3.55, 0.0058),
"LIN": ("Linde plc", 418.3, -0.0270, -11.61, 0.0057),
"QCOM": ("Qualcomm", 180.9, -0.0205, 3.64, 0.0057),
"PDD": ("PDD Holdings", 134.87, -0.0084, -1.14, 0.0056),
"INTC": ("Intel", 39.99, -0.0042, -0.17, 0.0056),
"ISRG": ("Intuitive Surgical", 534.28, -0.0080, 4.26, 0.0055),
"INTU": ("Intuit", 667.55, -0.0173, 11.37, 0.0054),
"AMAT": ("Applied Materials", 233.1, -0.0024, 0.55, 0.0054),
"ARM": ("Arm Holdings", 169.82, -0.0264, 4.37, 0.0053),
"BKNG": ("Booking Holdings", 5077.74, -0.0005, -2.47, 0.0048),
"AMGN": ("Amgen", 298.43, -0.0220, 6.43, 0.0047),
"KLAC": ("KLA Corporation", 1208.74, -0.0047, -5.67, 0.0047),
"PANW": ("Palo Alto Networks", 220.24, -0.0090, 1.97, 0.0044),
"GILD": ("Gilead Sciences", 119.79, -0.0114, 1.35, 0.0044),
"TXN": ("Texas Instruments", 161.46, -0.0059, 0.95, 0.0043),
"ADBE": ("Adobe Inc.", 340.31, -0.0032, 1.07, 0.0042),
"CRWD": ("CrowdStrike", 543.01, -0.0080, 4.33, 0.0040),
"HON": ("Honeywell", 201.33, -0.0061, 1.22, 0.0037),
"MELI": ("MercadoLibre", 2327.26, -0.0142, -33.5, 0.0035),
"CEG": ("Constellation Energy", 377, -0.0143, -5.48, 0.0034),
"ADI": ("Analog Devices", 234.13, -0.0053, 1.23, 0.0034),
"VRTX": ("Vertex Pharmaceuticals", 425.57, -0.0135, 5.68, 0.0032),
"DASH": ("DoorDash", 254.37, -0.0012, 0.3, 0.0032),
"ADP": ("ADP", 260.3, -0.0047, -1.23, 0.0031),
"CMCSA": ("Comcast", 27.84, -0.0189, 0.52, 0.0030),
"CDNS": ("Cadence Design Systems", 338.69, -0.0077, 2.6, 0.0027),
"SBUX": ("Starbucks", 80.87, -0.0274, -2.28, 0.0027),
"SNPS": ("Synopsys", 453.82, -0.0246, 10.89, 0.0025),
"MRVL": ("Marvell Technology", 93.74, -0.0584, 5.17, 0.0024),
"ORLY": ("O'Reilly Automotive", 94.44, -0.0075, -0.71, 0.0023),
"ABNB": ("Airbnb", 126.54, -0.0016, 0.2, 0.0023),
"MSTR": ("MicroStrategy Inc.", 269.51, -0.0587, 14.94, 0.0023),
"MDLZ": ("Mondelez International", 57.46, -0.0055, -0.31, 0.0022),
"CTAS": ("Cintas", 183.27, -0.0039, -0.71, 0.0022),
"MAR": ("Marriott International", 260.58, -0.0064, -1.69, 0.0021),
"TRI": ("Thomson Reuters Corporation", 153.06, -0.0093, -1.43, 0.0020),
"REGN": ("Regeneron Pharmaceuticals", 651.8, -0.0034, -2.24, 0.0020),
"CSX": ("CSX Corporation", 36.02, -0.0107, 0.38, 0.0020),
"FTNT": ("Fortinet", 86.43, -0.0265, 2.23, 0.0019),
"MNST": ("Monster Beverage", 66.83, -0.0039, 0.26, 0.0019),
"PYPL": ("PayPal", 69.27, -0.0197, 1.34, 0.0019),
"AEP": ("American Electric Power", 120.26, -0.0134, -1.63, 0.0019),
"ADSK": ("Autodesk", 301.34, -0.0019, 0.57, 0.0019),
"WDAY": ("Workday Inc.", 239.92, -0.0303, 7.05, 0.0019),
"AXON": ("Axon Enterprise Inc.", 732.23, -0.0090, -6.65, 0.0017),
"DDOG": ("Datadog", 162.81, -0.0365, 5.74, 0.0017),
"WBD": ("Warner Bros. Discovery", 22.45, -0.0384, 0.83, 0.0016),
"NXPI": ("NXP Semiconductors", 209.12, -0.0133, 2.74, 0.0015),
"ZS": ("Zscaler", 331.14, -0.0283, 9.1, 0.0015),
"ROST": ("Ross Stores", 158.92, -0.0054, 0.85, 0.0015),
"PCAR": ("Paccar", 98.4, -0.0043, -0.42, 0.0015),
"IDXX": ("Idexx Laboratories", 629.51, -0.0015, 0.97, 0.0015),
"EA": ("Electronic Arts", 200.06, -0.0007, 0.14, 0.0015),
"XEL": ("Xcel Energy", 81.17, -0.0051, -0.42, 0.0014),
"ROP": ("Roper Technologies", 446.15, -0.0062, 2.75, 0.0014),
"BKR": ("Baker Hughes", 48.41, -0.0035, -0.17, 0.0014),
"TTWO": ("Take-Two Interactive", 256.37, -0.0142, 3.59, 0.0014),
"FAST": ("Fastenal", 41.15, -0.0096, -0.4, 0.0014),
"EXC": ("Exelon", 46.12, -0.0202, -0.95, 0.0014),
"TEAM": ("Atlassian", 169.42, -0.0545, 8.75, 0.0013),
"PAYX": ("Paychex", 117.03, -0.0017, -0.2, 0.0012),
"CPRT": ("Copart", 43.01, -0.0125, 0.53, 0.0012),
"FANG": ("Diamondback Energy", 143.19, -0.0073, 1.04, 0.0012),
"CCEP": ("Coca-Cola Europacific Partners", 88.83, -0.0013, -0.12, 0.0012),
"KDP": ("Keurig Dr Pepper", 27.16, -0.0188, -0.52, 0.0011),
"CTSH": ("Cognizant", 72.88, -0.0096, 0.69, 0.0010),
"GEHC": ("GE HealthCare", 74.95, -0.0007, -0.05, 0.0010),
"MCHP": ("Microchip Technology", 62.42, -0.0056, 0.35, 0.0010),
"VRSK": ("Verisk", 218.76, -0.0053, 1.16, 0.0009),
"CHTR": ("Charter Communications", 233.84, -0.0126, 2.92, 0.0009),
"ODFL": ("Old Dominion Freight Line", 140.42, -0.0231, 3.17, 0.0009),
"KHC": ("Kraft Heinz", 24.73, -0.0061, 0.15, 0.0009),
"CSGP": ("CoStar Group", 68.81, -0.0119, -0.83, 0.0009),
"TTD": ("Trade Desk (The)", 50.28, -0.0268, 1.31, 0.0007),
"DXCM": ("DexCom", 58.22, -0.1463, -9.98, 0.0007),
"BIIB": ("Biogen", 154.27, -0.0311, 4.66, 0.0007),
"CDW": ("CDW Corporation", 159.37, -0.0164, 2.57, 0.0006),
"ON": ("Onsemi", 50.08, -0.0151, -0.77, 0.0006),
"LULU": ("Lululemon Athletica", 170.54, -0.0150, 2.52, 0.0006),
"GFS": ("GlobalFoundries", 35.6, -0.0128, -0.46, 0.0006)
}

INTRODUCTION_MESSAGE: Final[str] = (
    "Welcome to press your luck investments!\n"
    "We offer immediate returns under his breath *or losses*.\n"
    "Just tell me which how much and which stock and we'll see if you are "
    "a winner!")

INVESTMENT_INPUT: Final[str] = (
    "How much money are you willing to wager...erm I mean invest? "
)

# Filter for valid dollars and cents pattern (No $).
INVESTMENT_RE: Final[re.Pattern[str]] = re.compile("^\d*\.?\d{1,2}$")

INVESTMENT_ERROR: Final[str] = (
    "Please! only smackers and cents style! E.g. 123 or 123.45 or .3 or 0.33"
)

STOCK_SYMBOL_INPUT: Final[str] = (
    "Enter the stock you want to bet...I mean invest in\n"
    "('L' for a list of available stocks): "
)

# Filter for potential valid stick ticker.
STOCK_SYMBOL_RE: Final[re.Pattern[str]] = re.compile("^[A-Z]{1,5}$", re.IGNORECASE)

STOCK_SYMBOL_ERROR: Final[str] = (
    "Only between two to four capital letters allowed!"
)

STOCK_SYMBOL_LOOKUP_ERROR = (
    f"{'?'*79}\n"
    "Stock Symbol not found, enter 'L' for a list of available stocks.\n"
    f"{'?'*79}"
)

# ====================
# Logic Functions
# ====================
def get_data(
        input_message: str,
        re_pattern: re.Pattern[str],
        error_message: str,
        mode: Literal["money", "symbol"]
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
            if value.upper() == "L" and mode == "symbol":
                stock_symbol_string = ", ".join(STOCKS_DICT.keys())
                print(textwrap.fill(stock_symbol_string, width=79))
                continue
            if not re_pattern.fullmatch(value):
                raise ValueError(error_message)
            return value
        except ValueError as error:
            print(f"{'!'*79}\n{error}\n{'!'*79}")


def get_valid_stock() -> tuple[str,str,float,float,float,float]:
    """
    Extracts the record for a given stock symbol

    Returns
    -------
    a tuple of (stock_symbol,
                name,
                price,
                point_change,
                percent_change,
                weight
                )

    """
    while True:
        raw_stock_symbol = get_data(
            STOCK_SYMBOL_INPUT,
            STOCK_SYMBOL_RE,
            STOCK_SYMBOL_ERROR,
            "symbol"
        )
        if raw_stock_symbol in STOCKS_DICT:
            (name,
             price,
             point_change,
             percent_change,
             weight) = (
                STOCKS_DICT.get(raw_stock_symbol
                )
            )
            return (
                raw_stock_symbol,
                name,
                price,
                point_change,
                percent_change,
                weight
            )
        else:
            print(STOCK_SYMBOL_LOOKUP_ERROR)


def get_Investment_price(stock):
    pass


def get_return_on_investment(
        stock: tuple[str, str, float, float, float, float],
        investment: float
) -> float:
    profit_or_loss = investment * (1 + stock[4] / 100)
    if profit_or_loss < investment:
    return profit_or_loss


def main():
    print(INTRODUCTION_MESSAGE)
    stock = get_valid_stock()
    investment = float(get_data(
        INVESTMENT_INPUT,
        INVESTMENT_RE,
        INVESTMENT_ERROR,
        "money"
    ))
    investment_stock_price = get_Investment_price(stock)
    return_on_investment = get_return_on_investment(stock, float(investment))
    print(
        f"{'='*79}\n"
        f"You invested in {stock[1]} for the amount of {investment}.\n"
        f"{stock[0]} is valued at {stock[2]}. "
        f"your net is {return_on_investment}.")

if __name__ == '__main__':
    main()
