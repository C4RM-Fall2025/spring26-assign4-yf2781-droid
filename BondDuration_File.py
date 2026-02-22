
def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    rate = y / ppy
    coupon = face * couponRate / ppy

    pv_total = 0.0
    weighted_pv_total = 0.0

    for t in range(1, periods + 1):
        if t < periods:
            cf = coupon
        else:
            cf = coupon + face

        pv = cf / ((1 + rate) ** t)

        pv_total += pv
        weighted_pv_total += t * pv

    bondDuration = weighted_pv_total / pv_total

    return bondDuration
