
import sys
from matrix_io import MyList, print_update_matrix, do_update_choice, updated_matrix

matrix, n = do_update_choice(updated_matrix)

# Проходим по всем строкам кроме последней
for i in range(1, n):
    # Проходим по оставшимся строкам
    for k in range(i + 1, n + 1):
        # Находим коэффициент преобразования для вычитания, чтобы обнулить элемент под главной диагональю
        conversion_factor = matrix[k][i] / matrix[i][i]
        # Вычитаем из текущей строки произведение строки с коэффициентом преобразования и ведущей строкой
        for j in range(i, (n + 1) + 1):
            matrix[k][j] = round(matrix[k][j] - matrix[i][j] * conversion_factor, 6)

print_update_matrix(matrix)

ans = MyList([0] * n)  # Создаем список для решений системы

try:
    ans[n] = round(matrix[n][n + 1] / matrix[n][n], 6)  # Находим последний корень
except ZeroDivisionError:
    print('Матрица либо несовместна, либо совместна и неопределена')
    sys.exit()

# Обратный ход для нахождения остальных неизвестных
for i in range(n - 1, 0, -1):
    amount = 0
    # Проходим от диагонального элемента не включительно до конца строки
    for j in range(i + 1, n + 1):
        # Вычисляем сумму произведений коэффициентов и найденных значений для неизвестных
        amount += matrix[i][j] * ans[j]
    # Находим значение неизвестных
    ans[i] = round((matrix[i][n + 1] - amount) / matrix[i][i], 6)

print(f'Решение {ans}')
