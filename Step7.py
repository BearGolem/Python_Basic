#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix():
    some_data = []

    def __init__(self, some_data):
        self.some_data = some_data

    def __str__(self):
        new_str = ''
        for i in self.some_data:
            for j in i:
                new_str = new_str + f"{j:>10}"
            new_str = new_str + "\n"
        return new_str

    def __add__(self, other):
        result = self.some_data
        if len(self.some_data) != len(other.some_data):
            return f"Матрицы имеют разный размер"
            for i in range(len(self.some_data)):
                if len(self.some_data[i]) != len(other.some_data[i]):
                    return f"Матрицы имеют разный размер"

        for i in range(len(self.some_data)):
            if len(self.some_data[i]) != len(other.some_data[i]):
                return f"Матрицы имеют разный размер"

        for i in range(len(self.some_data)):
            for j in range(len(self.some_data[i])):
                result[i][j] = self.some_data[i][j] + other.some_data[i][j]
        return Matrix(result)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix1)
print(matrix1 + matrix2)


#Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Gucci_clothes(ABC):

    def __init__(self, rags_size):
        self.rags_size = rags_size

class Gucci_coat(Gucci_clothes):

    def __init__(self, rags_size):
        super().__init__(rags_size)

    @property
    def cloth_amount(self):
        return round(self.rags_size/6.5 + 0.5, 1)

class Gucci_suit(Gucci_clothes):

    def __init__(self, rags_size):
        super().__init__(rags_size)

    @property
    def cloth_amount(self):
        return round(self.rags_size * 2 + 0.3, 1)

rags1 = Gucci_suit(1.71)
rags2 = Gucci_coat(52)

print(rags1.cloth_amount, "\n", rags2.cloth_amount)


#Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

import inspect

class Cell:

    def __init__(self, cells_count):
        self.cells_count = cells_count


    def __add__(self, other):
        new_cell = self.cells_count + other.cells_count
        return Cell(new_cell)

    def __sub__(self, other):
        if self.cells_count > other.cells_count:
            new_cell = self.cells_count - other.cells_count
            return Cell(new_cell)
        else:
            return 'Mailfunction! Count of cell become to zero or below!'

    def __mul__(self, other):
        new_cell = self.cells_count * other.cells_count
        return Cell(new_cell)

    def __truediv__(self, other):
        new_cell = int(round(self.cells_count / other.cells_count, 0))
        return Cell(new_cell)

    def make_order(self, len_row):
        return "Cell looks like that:\n{}".format(('*' * len_row + "\n") *  (self.cells_count // len_row) + '*' * (self.cells_count % len_row))

cell1 = Cell(15)
cell2 = Cell(3)
cell3 = Cell(2)
print(cell1.make_order(5))
print((cell1 / cell3).make_order(7))
