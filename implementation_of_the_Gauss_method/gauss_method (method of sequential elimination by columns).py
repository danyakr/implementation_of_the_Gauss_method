
import sys
from matrix_io import print_matrix2, do_choice, matrix, NUMBER_OF_DECIMAL_PLACES

# Получаем матрицу и её размер для работы с пользователем
matrix, n = do_choice(matrix)

# Проходим по всем строкам кроме последней
for i in range(n - 1):
    lead_element = matrix[i][i]  # Вычисляем ведущий элемент для текущей строки
    # Делим все элементы текущей строки на ведущий элемент (приведение к единичному элементу на главной диагонали)
    for j in range(i, n + 1):
        matrix[i][j] = round(matrix[i][j] / lead_element, NUMBER_OF_DECIMAL_PLACES)

    # Проходим по оставшимся строкам
    for k in range(i + 1, n):
        conversion_factor = matrix[k][i]  # Определяем коэффициент преобразования для вычитания
        # Вычитаем из текущей строки произведение строки с множителем и опорной строкой
        # (делаем нули под главной диагональю)
        for j in range(i, n + 1):
            matrix[k][j] = round(matrix[k][j] - matrix[i][j] * conversion_factor, NUMBER_OF_DECIMAL_PLACES)

print_matrix2(matrix)

ans = [0] * n  # Создаем список для решений системы

try:
    ans[n - 1] = round(matrix[n - 1][n] / matrix[n - 1][n - 1], NUMBER_OF_DECIMAL_PLACES)  # Находим значение последнего корня
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
    # Вычитаем полученную сумму из свободного члена уравнения
    ans[i] = round(matrix[i][n] - amount, NUMBER_OF_DECIMAL_PLACES)

print(f'Решение {ans}')
