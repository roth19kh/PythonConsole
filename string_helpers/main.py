def convertToKHR(amount: float) -> str:
    """
    Convert an amount in USD to Cambodian Riel (KHR).

    Args:
        amount (float): The amount in USD.

    Returns:
        str: The converted amount in KHR as a string.
    """
    amount = amount * 4100
    return str(amount)

def calculateDiscount(discount: int, total: float) -> str:
    """
    Calculate the discount amount based on a discount percentage.

    Args:
        discount (int): The discount percentage.
        total (float): The total price before discount.

    Returns:
        str: The discount amount as a string.
    """
    disPrice = discount * total / 100
    return str(disPrice)

def formatNumber(number: float, place: int = 2) -> str:
    """
    Format a number with commas and a specified number of decimal places.

    Args:
        number (float): The number to format.
        place (int, optional): The number of decimal places (default is 2).

    Returns:
        str: The formatted number as a string.
    """
    return f"{float(number):,.{place}f}"