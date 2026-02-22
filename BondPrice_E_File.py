

def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    bondPrice = 0.0
    m = len(yc)

    for i, y in enumerate(yc, start=1):
        if i < m:
            cf = coupon
        else:
            cf = coupon + face

        pv = cf / ((1 + y) ** i)
        bondPrice += pv

    return bondPrice