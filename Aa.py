import math

# Универсальный метод дихотомии
def bisection(f, a, b, eps=0.0001):
    if f(a) * f(b) > 0:
        raise ValueError("На данном интервале нет смены знака!")

    iteration = 0
    print(f"{'№':<3} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<15}")

    while abs(b - a) > eps:
        c = (a + b) / 2
        fc = f(c)

        iteration += 1
        print(f"{iteration:<3} {a:<12.6f} {b:<12.6f} {c:<12.6f} {fc:<15.8f}")

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# ===============================
# Уравнение 1: x^2 + 4sin(x) = 0
# ===============================

def f1(x):
    return x**2 + 4 * math.sin(x)

print("\nУравнение 1: x^2 + 4sin(x) = 0")

# Корень на [-2, -1]
root1 = bisection(f1, -2, -1)
print("\nКорень 1 ≈", round(root1, 6))

# Корень x = 0 (точный)
print("Корень 2 = 0")


# ==========================================
# Уравнение 2: x^3 + 0.2x^2 + 0.5x + 0.8 = 0
# ==========================================

def f2(x):
    return x**3 + 0.2*x**2 + 0.5*x + 0.8

print("\nУравнение 2: x^3 + 0.2x^2 + 0.5x + 0.8 = 0")

root2 = bisection(f2, -1, 0)
print("\nКорень ≈", round(root2, 6))
