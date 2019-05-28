#can't keep a good man down
def pCal(gAmt,a,b):
    gAmt = int(gAmt)
    nd = {}
    for x in range(gAmt + 1):
        nd[gAmt - x] = x
    for y in range(a):
        del nd[a-1-y]
    for z in range(b):
        del nd[(int(gAmt)-b)+1+z]
    nd = list(nd.items())
    tpos = len(nd)
    try:
        os = round(100 * s / lowerBound, 1)
    except:
        os = 50
    s = 0
    lowerBound = 2 ** (nd[0][0] - a)
    for e in range(len(nd)):
        pA = nd[e][0] - a
        pB = nd[e][1] - b
        if nd[e][1] > nd[e][0]:
            continue
        s += factorial(pA + pB) / (factorial(pA) * factorial(pB))
    print(f"Percent chance of not losing: {round(100 * s / lowerBound) if round(100 * s / lowerBound, 1).is_integer() else round(100 * s / lowerBound, 1)}% ({'+' + str(round(100 * s / lowerBound - os, 1)) if round(100 * s / lowerBound - os, 1) > 0 else round(100 * s / lowerBound - os, 1)}%)")
