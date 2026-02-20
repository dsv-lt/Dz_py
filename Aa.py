import math


def bisection_table(f, a, b, eps=0.0001):
    k = 0

    print("{:<3} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "k", "a", "b", "c", "f(a)", "f(b)", "f(c)", "|b-a|"
    ))

    while abs(b - a) >= eps:
        c = round((a + b) / 2.0, 6)

        fa = round(f(a), 6)
        fb = round(f(b), 6)
        fc = round(f(c), 6)

        diff = round(abs(b - a), 6)

        print("{:<3} {:<12.6f} {:<12.6f} {:<12.6f} {:<12} {:<12} {:<12} {:<12}".format(
            k, a, b, c, fa, fb, fc, diff
        ))

        if fa * fc < 0:
            b = c
        else:
            a = c

        k += 1

    return round((a + b) / 2.0, 6)


# ===============================
# Уравнение 1
# x^2 + 4sin(x) = 0
# ===============================

def f1(x):
    return x * x + 4 * math.sin(x)


print("Уравнение 1")

root1 = bisection_table(f1, -2.0, -1.0)
print("Ответ:", root1)
print("Второй корень: 0.000000")


# ===============================
# Уравнение 2
# x^3 + 0.2x^2 + 0.5x + 0.8 = 0
# ===============================

def f2(x):
    return x**3 + 0.2 * x**2 + 0.5 * x + 0.8


print("\nУравнение 2")

root2 = bisection_table(f2, -1.0, 0.0)
print("Ответ:", root2)
