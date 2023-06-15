class Matrix():

    def __init__(self) -> None:
        self.number_of_lines = 0
        self.number_of_columns = 0
        return

    def input_matrix(self):
        self.number_of_lines = int(input('Введите количество строк: '))
        self.number_of_columns = int(input('Введите количество столбцов: '))
        self.arr = [[[] for i in range(self.number_of_columns)] for j in range(self.number_of_lines)]

        for i in range(self.number_of_lines):
            for j in range(self.number_of_columns):
                print('Введите значение (', i, ',', j, ') =', end='')
                self.arr[i][j] = input(' ')
        return

    def print_matrix(self, sign):
        print(sign)
        for i in range(self.number_of_lines):
            print(self.arr[i])
        return

    def matrix_content(self):
        print('Матрица содержит:\nКоличество строк:', self.number_of_lines, '\nКоличество столбцов:',
              self.number_of_columns)
        return

    def matrix_change(self):
        i = int(input('Введите номер строки: '))
        j = int(input('Введите номер колонки: '))
        new_value = input('Введите новое значение: ')
        self.arr[i - 1][j - 1] = new_value
        return

    def make_changes_matrix(make):
        make = input('Хотите внести изменения в матрицу? Введите ответ: да/нет ')
        if make == 'да':
            conclusion.matrix_change()
            conclusion.print_matrix('Матрица изменена:')
        elif make == 'нет':
            print('Конец операции.')
        else:
            print('Ошибка')
        return


conclusion = Matrix()
conclusion.input_matrix()
conclusion.print_matrix('Создана матрица:')
conclusion.matrix_content()
conclusion.make_changes_matrix()
print('Конец операции.')