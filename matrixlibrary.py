# Definisikan matriks A, B, C, D, dan E
A = [
    [3, 0],
    [-1, 2],
    [1, 1]
]

B = [
    [4, -1],
    [0, 2]
]

C = [
    [1, 4, 2],
    [3, 1, 5]
]

D = [
    [1, 5, 2],
    [-1, 0, 1],
    [3, 2, 4]
]

E = [
    [6, 1, 3],
    [-1, 1, 2],
    [4, 1, 3]
]

# Fungsi perkalian matriks manual
def multiply_matrices(X, Y):
    rows_X, cols_X = len(X), len(X[0])
    rows_Y, cols_Y = len(Y), len(Y[0])

    if cols_X != rows_Y:
        return "Perkalian tidak terdefinisi karena ukuran matriks tidak sesuai."

    result = [[0 for _ in range(cols_Y)] for _ in range(rows_X)]
    for i in range(rows_X):
        for j in range(cols_Y):
            for k in range(cols_X):
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Fungsi penjumlahan atau pengurangan matriks manual
def add_subtract_matrices(X, Y, operation):
    rows_X, cols_X = len(X), len(X[0])
    rows_Y, cols_Y = len(Y), len(Y[0])

    if rows_X != rows_Y or cols_X != cols_Y:
        return "Penjumlahan/Pengurangan tidak terdefinisi karena ukuran matriks tidak sesuai."

    result = [[0 for _ in range(cols_X)] for _ in range(rows_X)]
    for i in range(rows_X):
        for j in range(cols_X):
            if operation == 'add':
                result[i][j] = X[i][j] + Y[i][j]
            elif operation == 'subtract':
                result[i][j] = X[i][j] - Y[i][j]
    return result

# Perkalian matriks A x C
result_A_C = multiply_matrices(A, C)
print("Hasil perkalian A x C tanpa pustaka:")
print(result_A_C)

# Perkalian matriks A x B
result_A_B = multiply_matrices(A, B)
print("\nHasil perkalian A x B tanpa pustaka:")
print(result_A_B)

# Penjumlahan matriks D + E
result_D_plus_E = add_subtract_matrices(D, E, 'add')
print("\nHasil penjumlahan D + E tanpa pustaka:")
print(result_D_plus_E)

# Pengurangan matriks D - E
result_D_minus_E = add_subtract_matrices(D, E, 'subtract')
print("\nHasil pengurangan D - E tanpa pustaka:")
print(result_D_minus_E)

import numpy as np

# Definisikan matriks A, B, C, D, dan E
A = np.array([[3, 0], [-1, 2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

# Perkalian matriks A x C
try:
    result_A_C = np.dot(A, C)
    print("Hasil perkalian A x C:")
    print(result_A_C)
except ValueError as e:
    print("Perkalian A x C tidak terdefinisi:", e)

# Perkalian matriks A x B
try:
    result_A_B = np.dot(A, B)
    print("\nHasil perkalian A x B:")
    print(result_A_B)
except ValueError as e:
    print("Perkalian A x B tidak terdefinisi:", e)

# Penjumlahan matriks D + E
try:
    result_D_plus_E = D + E
    print("\nHasil penjumlahan D + E:")
    print(result_D_plus_E)
except ValueError as e:
    print("Penjumlahan D + E tidak terdefinisi:", e)

# Pengurangan matriks D - E
try:
    result_D_minus_E = D - E
    print("\nHasil pengurangan D - E:")
    print(result_D_minus_E)
except ValueError as e:
    print("Pengurangan D - E tidak terdefinisi:", e)