def sq(a, n):
    i = a
    for m in range(1, n + 1):
        i = ((a / i) + i) / 2
        m += 1
    return i


def newton(n):

    sqrt3 = sq(3, 1000)

    a = 1 / (2 * 2**3)
    s = a / (2 * 1 + 1)

    for i in range(2, n + 1):
        a = a * (2 * i - 3) / (2 * i) / (2**2)  # Rekurentní výpočet a_i
        s += a / (2 * i + 1)

    o_pi_nion = 12 * (-sqrt3 / 8 + 0.5 - s)
    return o_pi_nion


print(sq(2, 100))
print(newton(100))
