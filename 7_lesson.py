import math
from abc import ABC, abstractmethod
#1
class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self, result=""):
        for i in range(len(self.lists)):
            result = result + "\t".join(map(str, self.lists[i]))+"\n"
        return f'{result}'

    def __add__(self, other, result=""):
        for i in range(len(self.lists)):
            for j in range(len(self.lists[i])):
                result = result + str(self.lists[i][j] + other.lists[i][j])+"\t"
            result = result +"\n"
        return result
print('Номер 1')
mx1 = Matrix([[3, 5, 32],[2, 4, 6], [-1, 64, -8]])
mx2 = Matrix([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print(mx1)
print(mx2)
print(mx1 + mx2)

#2
class Dres(ABC):
    name = ""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def expend(self):
        pass


class Coat(Dres):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size


    def expend(self):
        if self.size < 42 or self.size > 56:
            return f'К сожалению, вещи таких размеров не шьем.'
        return(f'На Ваше пальто {self.name} необходимо: {math.ceil(self.size/6.5 + 0.5)} метров ткани')


class Suit(Dres):
    def __init__(self, name, higth):
        super().__init__(name)
        self.__higth = higth

    @property
    def higth(self):
        return self.__higth

    @higth.setter
    def higth(self, higth):
        self.__higth = higth


    def expend(self):
        if self.higth < 1.1 or self.higth > 2.2:
            return f'К сожалению, вещи таких размеров не шьем. (Возможно Вы написали рост в см.)'
        return(f'На Ваш костюм {self.name} необходимо: {math.ceil(2 * self.__higth + 0.3)} метров ткани')


print('\n Номер 2')
coat = Coat('Мурр', 46)
print(coat.expend())
suit = Suit('тройка', 180)
print(suit.expend())
suit.higth = 1.8
print(suit.expend())

#3
class Cell:
    count = 0

    def __init__(self, count):
        self.count = count

    def __str__(self):
        return f'Результат дейстаия: {self.count}'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if (self.count - other.count) < 0:
            return 'Разность числа ячеек отрицательна'
        else:
            return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count / other.count)

    def make_order(self, result=""):
        for i in range(self.count):
            if i % 5 == 0:
                result = result + '|'
            result = result + '*'
        return result
print('\n Номер 3')
cell1 = Cell(26)
cell2 = Cell(3)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order())