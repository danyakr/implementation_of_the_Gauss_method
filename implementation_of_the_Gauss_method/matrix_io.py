class MyList(list):
    """ MyList is a list subclass with custom indexing behavior.
    It overrides the __getitem__ and __setitem__ methods
    to implement 1-based indexing instead of the standard 0-based
    indexing in the list class.
    """
    def __getitem__(self, index):
        if 1 <= index <= len(self):
            return super().__getitem__(index - 1)
        else:
            raise IndexError("Индекс за границами списка")

    def __setitem__(self, index, value):
        if 1 <= index <= len(self):
            super().__setitem__(index - 1, value)
        else:
            raise IndexError("Индекс за границами списка")


# Data that can be used to test the code
matrix = [
    [5, 7, 6, 5, 23.1],
    [7, 10, 8, 7, 32.1],
    [6, 8, 10, 9, 33.1],
    [5, 7, 9, 10, 31.1]
]

matrix2 = [
    [1, 2, 3, -2, 1],
    [2, -1, -2, -3, 2],
    [3, 2, -1, 2, -5],
    [2, -3, 2, 1, 11]
]

updated_matrix = MyList([
    MyList([5, 7, 6, 5, 23]),
    MyList([7, 10, 8, 7, 32]),
    MyList([6, 8, 10, 9, 33]),
    MyList([5, 7, 9, 10, 31])
])

updated_matrix2 = MyList([
    MyList([1, 2, 3, -2, 1]),
    MyList([2, -1, -2, -3, 2]),
    MyList([3, 2, -1, 2, -5]),
    MyList([2, -3, 2, 1, 11])
])


def print_update_matrix(matrix):
    """
    Prints the matrix with aligned spacing for a matrix with customized 1-based indexing.

    Calculates the maximum length of elements in the matrix to align the elements properly,
    then iterates through the matrix and prints each element with the appropriate spacing.

    Args:
    matrix: MyList, the matrix to be printed with customized indexing starting from 1
    """
    max_len = 0
    for i in range(1, len(matrix) + 1):
        for j in range(1, len(matrix[i]) + 1):
            if len(str(matrix[i][j])) > max_len:
                max_len = len(str(matrix[i][j]))

    for i in range(1, len(matrix) + 1):
        for j in range(1, len(matrix[i]) + 1):
            if j == len(matrix):
                delimiter = '|'
            else:
                delimiter = ''
            print(f'{matrix[i][j]:^{max_len}}  {delimiter} ', end='')
        print()
    print()


def enter_update_matrix():
    """
    Allows user to input a matrix with customized 1-based indexing for a system of equations.

    Prompts the user to input the size of the matrix, then the extended matrix for the system of equations.
    The elements should be entered separated by spaces, row by row.

    Returns:
    matrix: MyList, the entered matrix for the system of equations with customized 1-based indexing
    n: int, the size of the matrix
    """
    n = int(input('Введите размер матрицы: '))
    print('Введите расширенную матрицу системы (по строкам, элементы вводите через пробел): n')
    matrix = MyList([MyList([0] * (n + 1)) for _ in range(n)])

    for i in range(1, n + 1):
        el = [int(i) for i in input(': ').split()]
        for j in range(1, n + 2):
            matrix[i][j] = el[j - 1]
        print_update_matrix(matrix)
    return matrix, n


def do_update_choice(matrix):
    """
    Allows user to choose an action regarding the matrix update with customized 1-based indexing.

    Prompts the user to choose between entering a new matrix or
    using a predefined example for matrix update.

    Args:
    matrix: MyList, the matrix to be used or displayed for update with customized indexing starting from 1

    Returns:
    matrix: MyList, the chosen or entered matrix for update with customized indexing starting from 1
    n: int, the size of the matrix for update
    """
    print('Выберите цифру')
    print('1. Ввести матрицу')
    print('2. Использовать контрольный пример')
    choice = int(input(': '))
    if choice == 1:
        return enter_update_matrix()
    else:
        print_update_matrix(matrix)
        return matrix, len(matrix)


def print_matrix(matrix):
    """
    Prints the matrix with aligned spacing.

    Calculates the maximum length of elements in the matrix to align the elements properly,
    then iterates through the matrix and prints each element with the appropriate spacing.
    """
    max_len = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(str(matrix[i][j])) > max_len:
                max_len = len(str(matrix[i][j]))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix):
                delimiter = '|'
            else:
                delimiter = ''
            print(f'{delimiter} {matrix[i][j]:^{max_len}}  ', end='')
        print()
    print()


def enter_matrix():
    """
    Allows user to input a matrix for a system of equations.

    Prompts the user to input the size of the matrix, then the extended matrix for the system of equations.
    The elements should be entered separated by spaces, row by row.
    """
    n = int(input('Введите размер матрицы: '))
    print('Введите расширенную матрицу системы (по строкам, элементы вводите через пробел): n')
    matrix = [[0] * (n + 1) for _ in range(n)]

    for i in range(n):
        el = [int(i) for i in input(': ').split()]
        for j in range(n + 1):
            matrix[i][j] = el[j]
        print_matrix(matrix)
    return matrix, n


def do_choice(matrix):
    """
    Allows user to choose an action regarding the matrix.

    Prompts the user to choose between entering a new matrix or using a predefined example.
    """
    print('Выберите цифру')
    print('1. Ввести матрицу')
    print('2. Использовать контрольный пример')
    choice = int(input(': '))
    if choice == 1:
        return enter_matrix()
    else:
        print_matrix(matrix)
        return matrix, len(matrix)
