import numpy as np
# №1
def get_minor(matrix, i, j):
    return np.delete(np.delete(matrix, i, axis=0), j, axis=1)
def my_det(matrix):
    n = matrix.shape[0]
    if n == 1:
        return matrix[0, 0]
    if n == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    det1 = 0
    for col in range(n):
        sign = (-1) ** col
        sub_det = my_det(get_minor(matrix, 0, col))
        det1 += sign * matrix[0, col] * sub_det
    return det1
# №2
def my_eig_2x2(matrix):
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]
    tr = a + d
    det2 = a * d - b * c
    dis = tr**2 - 4 * det2
    l1 = (tr - np.sqrt(dis)) /2
    l2 = (tr + np.sqrt(dis)) /2
    vals = [l1, l2]
    vecs = []
    for lam in vals:
        if abs(b) > 1e-9:
            v = np.array([b, lam - a])
        elif abs(c) > 1e-9:
            v = np.array([lam - d, c])
        else:
            v = np.array([1, 0]) if lam == a else np.array([0, 1])
        v = v / np.linalg.norm(v)
        vecs.append(v)
    return np.array(vals), np.array(vecs).T
# проверка
print("\nlab_5")
n = 4
A = np.random.randint(-5, 5, (n, n))
print(f"Матрица A ({n}x{n}):\n{A}")
d_my = my_det(A)
d_np = np.linalg.det(A)
print(f"Мой Det: {d_my}")
print(f"NumPy Det: {d_np:.2f}")
print("-" * 20)
B2 = np.random.randint(1, 10, (2, 2))
A2 = np.array([[4, 1], [2, 3]])
print(f"Матрица 2x2:\n{A2}")
val_my, vec_my = my_eig_2x2(A2)
val_np, vec_np = np.linalg.eig(A2)
print(f"Мои собств. значения: {val_my}")
print(f"NumPy собств. значения: {val_np}")
print(f"Мои собств. вектора:\n{vec_my}")

print(f"NumPy собств. вектора:\n{vec_np}")

import numpy as np
def determinant(matrix):
    """Вычисление определителя методом разложения по первой строке"""
    n = matrix.shape[0]
    if n == 1:
        return matrix[0, 0]
    if n == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    det = 0
    for j in range(n):
        minor = np.delete(np.delete(matrix, 0, axis=0), j, axis=1)
        cofactor = ((-1) ** j) * matrix[0, j] * determinant(minor)
        det += cofactor
    return det
n = int(input("Введите размерность матрицы: "))
A = np.random.randint(-10, 10, (n, n)).astype(float)
print("Матрица A:")
print(A)
my_det = determinant(A)
numpy_det = np.linalg.det(A)
print(f"\nМой определитель: {my_det}")
print(f"NumPy определитель: {numpy_det}")
print(f"Разница: {abs(my_det - numpy_det)}")
