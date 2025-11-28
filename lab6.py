import numpy as np
def get_det(M):
    return np.linalg.det(M)
def get_cofactor_matrix(M):
    n = M.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(M, i, axis=0), j, axis=1)
            C[i, j] = ((-1) ** (i + j)) * get_det(minor)
    return C
def my_inverse(M):
    det = get_det(M)
    if abs(det) < 1e-9:
        raise ValueError("Матрица вырождена, обратной нет")
    C = get_cofactor_matrix(M)
    return C.T / det
# №1
def cramer_solve(A, b):
    n = A.shape[0]
    det_A = get_det(A)
    if abs(det_A) < 1e-9:
        return None
    x = np.zeros(n)
    for i in range(n):
        A_temp = A.copy()
        A_temp[:, i] = b
        x[i] = get_det(A_temp) / det_A
    return x
# №2
def solve_matrix_equation(variant, A=None, B=None, C=None):
    if variant == 1:
        A_inv = my_inverse(A)
        return A_inv @ B
    elif variant == 2:
        A_inv = my_inverse(A)
        return B @ A_inv
    elif variant == 3:
        A_inv = my_inverse(A)
        C_inv = my_inverse(C)
        return A_inv @ B @ C_inv
    return None
# проверка
print("\nлаб_6")
# 1. Крамер
n = 3
A = np.random.randint(1, 10, (n, n))
b = np.random.randint(1, 10, n)
print("Матрица A:\n", A)
print("Вектор b:", b)
x_cramer = cramer_solve(A, b)
x_numpy = np.linalg.solve(A, b)
print("Решение Крамером:", x_cramer)
print("Решение NumPy:   ", x_numpy)
# 2. Матричные уравнения
print("\n--- Матричное уравнение AX = B ---")
B_mat = np.random.randint(1, 10, (n, 2))
X_custom = solve_matrix_equation(1, A=A, B=B_mat)
# Проверка: X = A^(-1)B
X_numpy_eq = np.linalg.inv(A) @ B_mat
print("Мое решение X:\n", X_custom)
print("Проверка NumPy (inv(A) @ B):\n", X_numpy_eq)