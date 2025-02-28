def convertToKHR(amount: float) -> str:
    amount = amount * 4100
    return str(amount)

def calculateDiscount( discount: int ,total: float) -> str:
    disPrice = discount * total /100
    return str(disPrice)

def formatNumber(number: float, place: int = 2) -> str:
    return f"{float(number):,.{place}f}"