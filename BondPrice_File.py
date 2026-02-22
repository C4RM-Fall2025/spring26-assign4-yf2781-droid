

def getBondPrice(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    rate = y / ppy
    coupon = face * couponRate / ppy

    bondPrice = 0.0

    for t in range(1, periods + 1):
        bondPrice += coupon / ((1 + rate) ** t)

    # add face value at maturity
    bondPrice += face / ((1 + rate) ** periods)

    return bondPrice