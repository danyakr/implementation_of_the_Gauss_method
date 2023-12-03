
import sys
from matrix_io import MyList, print_update_matrix2, do_update_choice, updated_matrix, NUMBER_OF_DECIMAL_PLACES


matrix, n = do_update_choice(updated_matrix)

# Проходим по всем строкам кроме последней
for i in range(1, n):
    lead_element = matrix[i][i]  # Вычисляем ведущий элемент для текущей строки
    # Делим всю текущую строку на ведущий элемент (приведение к единичному элементу на главной диагонали)
    for j in range(i, (n + 1) + 1):
        matrix[i][j] = round(matrix[i][j] / lead_element, NUMBER_OF_DECIMAL_PLACES)

    # Проходим по оставшимся строкам
    for k in range(i + 1, n + 1):
        conversion_factor = matrix[k][i]  # Коэффициент преобразования для вычитания
        # Вычитаем из текущей строки произведение строки с коэффициентом преобразования и ведущей строкой
        for j in range(i, (n + 1) + 1):
            matrix[k][j] = round(matrix[k][j] - matrix[i][j] * conversion_factor, NUMBER_OF_DECIMAL_PLACES)

print_update_matrix2(matrix)

ans = MyList([0] * n)  # Создаем список для решения системы

try:
    ans[n] = round(matrix[n][n + 1] / matrix[n][n], NUMBER_OF_DECIMAL_PLACES)  # Находим значение последнего корня
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
    ans[i] = round(matrix[i][n + 1] - amount, NUMBER_OF_DECIMAL_PLACES)

print(f'Решение {ans}')

