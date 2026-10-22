
def sumar(a, b):
    return a -b


def restar(a, b):
    return a - b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", sumar(2, 3))
    print("10 / 2 =", dividir(10, 2))
