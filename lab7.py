import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# №1
x = np.random.rand(10) * 10
y = np.random.rand(10) * 10
plt.figure(figsize=(12, 4))
plt.suptitle("Задание 1: Точки и линии")
# 1. Просто точки
plt.subplot(1, 3, 1)
plt.scatter(x, y, color='red', label='Points')
plt.title("Точки")
plt.grid(True)
plt.legend()
# 2. Линейный график
plt.subplot(1, 3, 2)
plt.plot(x, y, color='blue', linestyle='--', marker='o', label='Line')
plt.title("Линейный график")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.legend()
# 3. Замкнутая кривая (добавляем первую точку в конец)
x_closed = np.append(x, x[0])
y_closed = np.append(y, y[0])
plt.subplot(1, 3, 3)
plt.plot(x_closed, y_closed, color='green', linewidth=2, label='Loop')
plt.fill(x_closed, y_closed, color='lightgreen', alpha=0.3)
plt.title("Замкнутая кривая")
plt.gca().set_facecolor('#f0f0f0')
plt.legend()
plt.show()
# №2
t = np.linspace(0, 2*np.pi, 1000)
# фигура 1
x1 = np.sin(3*t)
y1 = np.sin(2*t)
# фигура 2
x2 = np.sin(5*t)
y2 = np.sin(4*t)
plt.figure(figsize=(10, 5))
plt.plot(x1, y1, label='3:2', color='purple')
plt.plot(x2, y2, label='5:4', color='orange', linestyle='-.')
plt.title("Фигуры Лиссажу")
plt.xlabel("sin(at)")
plt.ylabel("sin(bt)")
plt.legend()
plt.grid(True)
plt.show()
# №3
x_f = np.linspace(-5, 5, 100)
y_f1 = 5*x_f**3 + 2*x_f**2 - 7*x_f + 10
y_f2 = 3*x_f**2
plt.figure(figsize=(8, 6))
plt.plot(x_f, y_f1, label=r'$5x^3 + 2x^2 - 7x + 10$', color='crimson')
plt.plot(x_f, y_f2, label=r'$3x^2$', color='navy', linestyle='--')
plt.title("Графики функций")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.gca().set_facecolor('#eafff5')
plt.grid(True)
plt.show()
# №4
salary = np.random.uniform(10, 100, 50)
exp = np.random.uniform(1, 10, 50)
plt.figure(figsize=(12, 5))
# Гистограмма
plt.subplot(1, 2, 1)
# разделение по интервалам для раскраски вручную
grp1 = exp[(exp >= 1) & (exp < 4)]
grp2 = exp[(exp >= 4) & (exp < 7)]
grp3 = exp[(exp >= 7) & (exp <= 10)]
plt.hist([grp1, grp2, grp3], bins=[1, 4, 7, 10],
         color=['red', 'green', 'blue'], label=['1-3 года', '4-7 лет', '7-10 лет'],
         edgecolor='black')
plt.title("Гистограмма стажа")
plt.xlabel("Годы")
plt.ylabel("Количество")
plt.legend()
# Диаграмма рассеяния
plt.subplot(1, 2, 2)
plt.scatter(exp, salary, c='magenta', edgecolor='black', label='Сотрудники')
plt.title("Стаж vs ЗП")
plt.xlabel("Стаж (лет)")
plt.ylabel("Зарплата (усл. ед)")
plt.legend()
plt.grid(True)
plt.show()
# №5
theta = np.linspace(0, 2.*np.pi, 100)
phi = np.linspace(0, 2.*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
R, r = 5, 2
x_tor = (R + r*np.cos(theta)) * np.cos(phi)
y_tor = (R + r*np.cos(theta)) * np.sin(phi)
z_tor = r * np.sin(theta)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_tor, y_tor, z_tor, cmap='viridis', edgecolor='none')
ax.set_title("3D Top")
plt.show()