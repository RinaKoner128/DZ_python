#1
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, info):
        day, month, year = map(int, info.split('-'))
        return cls(day, month, year)

    @staticmethod
    def valid_date(obj):
        if obj.day < 32 and obj.month < 13:
            return f'Day: {obj.day}, month: {obj.month}, year: {obj.year}'
        else:
            return 'Введен неверный формат даты'

print(' Номер 1')
info = '12-05-2021'
date = Date.set_date(info)
print(Date.valid_date(date))

#2
print('\n Номер 2')
class Zerro(Exception):
    def __init__(self, txt):
        self.txt = txt

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
try:
    if b == 0:
        raise Zerro('Делить на "0" нельзя')
    print(f'Результат деления = {a / b}')
except Zerro as err:
    print(err)

#3
print('\n Номер 3')
class Type(Exception):
    def __init__(self, txt):
        self.txt = txt
a = ''
user_list = []
while a != 'stop':
    try:
        a = input('Введите значение: ')
        if a.isdigit():
            user_list.append(int(a))
        else:
            raise Type('В списке должны присутствовать только числа')
    except Type as err:
        print(err)
print(user_list)

#4-6
"""
Проект - "Магазин музыкальных инструментов"
Продавец осуществляет продажу клиенту духовых,
струнных и клавишных инструментов. После покупки
идет метод - доставка товара до клиента.
"""
class Person:
    def __init__(self, lastname, firstname, secondname, phone):
        self.lastname = lastname
        self.firstname = firstname
        self.secondname = secondname
        self.phone = phone

    def __str__(self):
        return f"ФИО: {self.lastname} {self.firstname} {self.secondname}\n Номер телефона: {self.phone}"


class Worker(Person):  #Сотрудник магазина
    def __init__(self, lastname, firstname, secondname, phone, potision):
        super().__init__(lastname, firstname, secondname, phone)
        self.potision = potision

    def sell(self, cl, *items):  #Метод отвечающий за продажу товара клиенту
        for item in items:
            cl.cart(str(item))


class Client(Person):  #Клиент
    def __init__(self, lastname, firstname, secondname, phone,  address):
        super().__init__(lastname, firstname, secondname, phone)
        self.address = address
        self.cart_list = []

    def cart(self, items):  #Метод сбора корзины клиента
        self.cart_list.append(items)

    def delivery(self):  #Оформление доставки покупки клиента
        print(f'{self.lastname} {self.firstname} {self.secondname}! Ваши товары:\n{self.cart_list} \nдоставят по адресу: {self.address}. ')


class Items:  #Товары
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f'{self.type} инструмент {self.name}'

class Brass(Items):  #Духовые инструменты
    def __init__(self, name, type, isorchestra):  #Уникальный параметр - оркестровый ли инструмент
        super().__init__(name, type)
        self.__isorchestra = isorchestra

    @property
    def isorchestra(self):
        return self.__isorchestra

    @isorchestra.setter
    def isorchestra(self, isorchestra):
        self.__isorchestra = isorchestra


class Strings(Items):  #Струнные инструменты
    def __init__(self, name, type, size):  #Уникальный параметр - размер инструмента
        super().__init__(name, type)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size



class Keyboards(Items):  #Клавишные инструменты
    def __init__(self, name, type, classification):  #Уникальный параметр - формат инструмента
        super().__init__(name, type)
        self.__classification = classification

    @property
    def classification(self):
        return self.__classification

    @classification.setter
    def classification(self, classification):
        self.__classification = classification

print('\n Номер 4-6')
brass = Brass('Кларнет', 'Духовой', False)
string = Strings('Скрипка', 'Струнный', 3/4)
key = Keyboards('Рояль', 'Клавишный', 'электронный')
w = Worker('Иванова', 'Екатерина', 'Ивановна', '80004006000', 'кассир')
c = Client('Иванова', 'Екатерина', 'Ивановна', '80004006000', 'г.Радости, пер.Счастья, 100-500')
w.sell(c, string, key, brass)
c.delivery()

#7
def sign(a, b):
    if b > 0:
        result = f'{a} + {b}i'
    elif b < 0:
        result = f'{a} - {b * (-1)}i'
    else:
        result = f'{a}'
    return result

class Complex:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return f'Результат дейстаия: {self.numbers}'

    def __add__(self, other, result=""):
        a = self.numbers[0] + other.numbers[0]
        b = self.numbers[1] + other.numbers[1]
        return Complex(sign(a, b))

    def __mul__(self, other, result=""):
        a = self.numbers[0] * other.numbers[0] - self.numbers[1] * other.numbers[1]
        b = self.numbers[0] * other.numbers[1] + self.numbers[1] * other.numbers[0]
        return Complex(sign(a, b))

print('\n Номер 7')
c1 = Complex([1, -7])
c2 = Complex([4, -2])
print(c1 + c2)
print(c1 * c2)
