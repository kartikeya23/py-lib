def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def lcm(a, b):
    multiplier = 1
    while (multiplier * a) % b != 0:
        multiplier += 1
    return (multiplier * a)

def hcf(a, b):
    return a * b / lcm(a, b)

def numOfDgts(n):
    dgts = 0
    while(n > 0):
        dgts += 1
        n /= 10
    return dgts

def getDgts(n):
    Dgts = []
    while(n > 0):
        Dgts.insert(0, n % 10)
        n /= 10
    return Dgts

def isArmstrong(n):
    dgts = getDgts(n)
    power = len(dgts)
    total = 0
    for d in dgts:
        total += d ** power
    if total == n:
        return True
    else:
        return False
