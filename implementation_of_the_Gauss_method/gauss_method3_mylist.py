
import sys
from matrix_io import MyList, print_update_matrix, do_update_choice, updated_matrix

matrix, n = do_update_choice(updated_matrix)

# Проходим по всем строкам
for i in range(1, n + 1):
    # Проходим по оставшимся строкам, исключая ведущую строку
    for k in range(1, n + 1):
        if k == i:
            continue
        # Находим коэффициент преобразования для вычитания, чтобы обнулить элемент не стоящий на диагонали
        try:
            conversion_factor = matrix[k][i] / matrix[i][i]
        except ZeroDivisionError:
            print_update_matrix(matrix)
            print('Матрица либо несовместна, либо совместна и неопределена')
            sys.exit()
        # Вычитаем из текущей строки произведение строки с коэффициентом преобразования и ведущей строкой
        for j in range(i, (n + 1) + 1):
            if j == i:
                matrix[k][i] = 0
                continue
            matrix[k][j] = round(matrix[k][j] - matrix[i][j] * conversion_factor, 6)

print_update_matrix(matrix)

ans = MyList([0] * n)  # Создаем список для решений системы

# Проходим по диагонали и делим значение из столбца свободных членов на соответсвующий
# диагональный элемент из той же строки
for i in range(1, n + 1):
    ans[i] = round(matrix[i][n + 1] / matrix[i][i], 6)

print(f'Решение {ans}')
