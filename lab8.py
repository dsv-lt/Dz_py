import numpy as np
import matplotlib.pyplot as plt
# №1
print("\n=== ЛАБОРАТОРНАЯ 8 ===")
var1 = np.array([0, 1, 2, 3])
correlations = []
cosines = []
shifts = range(-50, 51)
for shift in shifts:
    var2 = var1 + shift
    # 1. корреляция Пирсона (центрированные вектора)
    v1_centered = var1 - np.mean(var1)
    v2_centered = var2 - np.mean(var2)
    numerator_p = np.dot(v1_centered, v2_centered)
    denominator_p = np.linalg.norm(v1_centered) * np.linalg.norm(v2_centered)
    pearson = numerator_p / denominator_p
    # 2. косинусное сходство (исходные вектора)
    numerator_c = np.dot(var1, var2)
    denominator_c = np.linalg.norm(var1) * np.linalg.norm(var2)
    cosine = numerator_c / denominator_c
    correlations.append(pearson)
    cosines.append(cosine)
# график
plt.figure(figsize=(10, 5))
plt.plot(shifts, correlations, label='Pearson Correlation', linestyle='--')
plt.plot(shifts, cosines, label='Cosine Similarity')
plt.xlabel("Смещение (Shift)")
plt.ylabel("Значение коэффициента")
plt.title("Влияние смещения на метрики сходства")
plt.legend()
plt.grid(True)
plt.show()
# №2-
# генерируем данные, похожие на оценки
# предположим 3 предмета (Math, Reading, Writing) для 20 студентов
np.random.seed(42)
data = np.random.randint(50, 100, (20, 3))
X = data  # матрица n строк (наблюдения), m столбцов (признаки)
# 1. Своя матрица ковариации
# Нужно центрировать столбцы!
X_centered = X - np.mean(X, axis=0)
n = X.shape[0]
# Формула: C = (X_T * X) / (n - 1)
C_custom = np.dot(X_centered.T, X_centered) / (n - 1)
# 2. Встроенная функция
C_numpy = np.cov(X, rowvar=False)
# 3. Разница
diff = C_custom - C_numpy
print("Custom Covariance Matrix:\n", C_custom)
print("Numpy Covariance Matrix:\n", C_numpy)
print("Difference (should be close to 0):\n", diff)
# Визуализация (Тепловые карты)
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
im1 = ax[0].imshow(C_custom, cmap='hot', interpolation='nearest')
ax[0].set_title("Моя ковариация")
plt.colorbar(im1, ax=ax[0])
im2 = ax[1].imshow(C_numpy, cmap='hot', interpolation='nearest')
ax[1].set_title("NumPy cov()")
plt.colorbar(im2, ax=ax[1])
im3 = ax[2].imshow(diff, cmap='coolwarm', interpolation='nearest')
ax[2].set_title("Разница")
plt.colorbar(im3, ax=ax[2])
plt.show()