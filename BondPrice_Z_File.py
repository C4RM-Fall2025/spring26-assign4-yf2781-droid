

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0.0

    for t, y in zip(times, yc):
        if t != times[-1]:
            cf = coupon
        else:
            cf = coupon + face

        pv = cf / ((1 + y) ** t)
        bondPrice += pv

    return bondPrice