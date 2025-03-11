def sq(a, n):
    i = a
    for m in range(1, n + 1):
        i = ((a / i) + i) / 2
    return i


def Archimedes(n):

    v = sq(1 - 0.25, 1000)  # výška šestiúhelníku
    z = 1  # základna šestiúhelníku
    sides = 6  # Počet stran mnohoúhelníku

    for i in range(1, n):
        z = sq((z / 2) ** 2 + (1 - v) ** 2, 1000)
        v = sq(1 - (z / 2) ** 2, 1000)
        sides *= 2
    return sides * z * v / 2


def Newton(n):

    a = 1 / (2 * (2 ** 3))
    s = a / (2 * 1 + 1)

    for i in range(2, n + 1):
        a = a * (2 * i - 3) / (2 * i) / (2 ** 2)
        s += a / (2 * i + 1)

    return 12 * (-sq(3, 1000) / 8 + 0.5 - s)


print(sq(2, 100))
print(Archimedes(100))
print(Newton(100))
