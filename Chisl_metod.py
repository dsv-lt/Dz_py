import math

# ---------- Задание 1 ----------
x1 = 0.16152
x1_approx = round(x1, 3 - int(math.floor(math.log10(abs(x1)))) - 1)
delta_abs_1 = abs(x1 - x1_approx)
delta_rel_1 = delta_abs_1 / abs(x1)

# ---------- Задание 2 ----------
x2 = 2.32
delta_rel_percent = 0.72
delta_abs_2 = x2 * (delta_rel_percent / 100)

# ---------- Задание 3 ----------
x3 = 0.1132
delta_abs_3 = 0.0001

# ---------- Задание 5 ----------
x5 = 3.142
F = x5 * math.log(x5)
delta_x5 = 0.0005
F_prime = math.log(x5) + 1
delta_F = abs(F_prime) * delta_x5
delta_rel_F = delta_F / abs(F)

# ---------- Задание 6 ----------
x1_6 = 3.28
x2_6 = 0.932
x3_6 = 1.132

u = (x1_6 + x2_6**2) / x3_6

dx1 = 0.005
dx2 = 0.0005
dx3 = 0.0005

du_dx1 = 1 / x3_6
du_dx2 = 2 * x2_6 / x3_6
du_dx3 = -(x1_6 + x2_6**2) / x3_6**2

delta_u = abs(du_dx1)*dx1 + abs(du_dx2)*dx2 + abs(du_dx3)*dx3
delta_rel_u = delta_u / abs(u)

print("Задание 1:", x1_approx, delta_abs_1, delta_rel_1)
print("Задание 2:", delta_abs_2)
print("Задание 5:", F, delta_F, delta_rel_F)
print("Задание 6:", u, delta_u, delta_rel_u)
