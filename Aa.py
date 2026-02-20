import math

def bisection_table(f, a, b, eps=0.0001):
    if f(a) * f(b) > 0:
        raise ValueError("На интервале нет смены знака")

    k = 0
    print(f"{'k':<3} {'a':<12} {'b':<12} {'c':<12} "
          f"{'f(a)':<12} {'f(b)':<12} {'f(c)':<12} {'|b-a|':<12}")

    while True:
        c = round((a + b) / 2, 6)
        fa = round(f(a), 6)
        fb = round(f(b), 6)
        fc = round(f(c), 6)
        diff = round(abs(b - a), 6)

        print(f"{k:<3} {a:<12.6f} {b:<12.6f} {c:<12.6f} "
              f"{fa:<12} {fb:<12} {fc:<12} {diff:<12}")

        if diff < eps:
            break

        if fa * fc < 0:
            b = c
        else:
            a = c

        k += 1

    return round((a + b) / 2, 6)


# ==================================
# Уравнение 1: x^2 + 4sin(x) = 0
# ==================================

def f1(x):
    return x**2 + 4 * math.sin(x)

print("\nУравнение 1")

root1 = bisection_table(f1, -2, -1)
print("\nОтвет:", root1)

print("Второй корень: 0.000000")


# ==========================================
# Уравнение 2: x^3 + 0.2x^2 + 0.5x + 0.8 = 0
# ==========================================

def f2(x):
    return x**3 + 0.2*x**2 + 0.5*x + 0.8

print("\nУравнение 2")

root2 = bisection_table(f2, -1, 0)
print("\nОтвет:", root2)
