from decimal import Decimal


def add(x, y):
    return str(Decimal(x) + Decimal(y))


def sub(x, y):
    return str(Decimal(x) - Decimal(y))


def mul(x, y):
    return str(Decimal(x) * Decimal(y))


def div(x, y):
    return str(Decimal(x) / Decimal(y))


def fact(x):
    if not x.isdigit():
        raise ValueError("Not whole number in factorial")

    return str(fact_evaluator(Decimal(x)))


def fact_evaluator(x):
    if x < 0:
        raise ValueError("Negative number in factorial")

    if x == 0 or x == 1:
        return 1

    return x * fact_evaluator(x - 1)


operation_list = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "!": fact
}
