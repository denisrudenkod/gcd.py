def gcd(a, b):
    """Find the greatest common divisor of two numbers"""
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
