"""Quadratic Identities
Write a menu-driven program using modules to calculate algebraic identities"""


# Supporting Module
# identities.py

def exp1(a, b):
    return a ** 2 + 2 * a * b + b ** 2


def exp2(a, b):
    return a ** 2 - 2 * a * b + b ** 2


def exp3(a, b):
    return (a + b) * (a - b)


def exp4(a, b):
    return (a + b) ** 2 - 2 * a * b


def exp5(a, b):
    return a ** 3 + 3 * a ** 2 * b + 3 * a * b ** 2 + b ** 3


def exp6(a, b):
    return a ** 3 - 3 * a ** 2 * b + 3 * a * b ** 2 - b ** 3
