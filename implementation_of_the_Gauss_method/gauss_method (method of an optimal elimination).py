
import sys
from matrix_io import print_matrix2, do_choice, matrix, NUMBER_OF_DECIMAL_PLACES

matrix, n = do_choice(matrix)

# Проходим по всем строкам кроме последней
for i in range(n - 1):
    # Проходим по оставшимся строкам
    for k in range(i + 1, n):
        # Находим коэффициент преобразования для вычитания, чтобы обнулить элемент под главной диагональю
        conversion_factor = matrix[k][i] / matrix[i][i]
        # Вычитаем из текущей строки произведение строки с коэффициентом преобразования и ведущей строкой
        for j in range(i, n + 1):
            matrix[k][j] = round(matrix[k][j] - matrix[i][j] * conversion_factor, NUMBER_OF_DECIMAL_PLACES)

print_matrix2(matrix)

ans = [0] * n  # Создаем список для решений системы

try:
    # Находим значение последнего корня
    ans[n - 1] = round(matrix[n - 1][n] / matrix[n - 1][n - 1], NUMBER_OF_DECIMAL_PLACES)
except ZeroDivisionError:
    print('Матрица либо несовместна, либо совместна и неопределена')
    sys.exit()

# Обратный ход для нахождения остальных неизвестных
for i in range(n - 2, -1, -1):
    amount = 0
    # Проходим от диагонального элемента не включительно до конца строки
    for j in range(i + 1, n):
        # Вычисляем сумму произведений коэффициентов и найденных значений для неизвестных
        amount += matrix[i][j] * ans[j]
    # Находим значение неизвестных
    ans[i] = round((matrix[i][n] - amount) / matrix[i][i], NUMBER_OF_DECIMAL_PLACES)

print(f'Решение {ans}')
