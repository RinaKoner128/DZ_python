import time
#1
class TrafficLight:
    __color = "red"

    def running(self):
        self.__color="red"
        print(f'{self.__color}')
        time.sleep(7)
        self.__color = "yellow"
        print(f'{self.__color}')
        time.sleep(2)
        self.__color = "green"
        print(f'{self.__color}')
        time.sleep(7)
print('"Светофор"')
traffic=TrafficLight()
traffic.running()

#2
class Road:
    _length = 0
    _width = 0

    def weight(self, _length, _width):
        self.l = _length
        self.w = _width
        print(f'Масса асфальта равна: {(self.l*self.w*25*5)/1000} т')

print('"Дорога"')
road=Road()
road.weight(20, 5000)

#3
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position, _income={}):
        super().__init__(name, surname, position)
        print(f'Сотрудник: {self.surname} {self.name} - {self.position}')
        self._income = _income

    def get_total_income(self):
        return sum(self._income.values())

print('"Офис"')
r = Position("Алексей", "Петров", "инженер", {"wage": 40000, "bonus": 17985})
print(f'Его доход составляет: {r.get_total_income()} рублей')

#4
class Car:
    speed = 0
    color = ""
    name = ""
    is_police = True

    def __init__(self, name, color, speed):
        self.speed = speed
        self.name = name
        self.color = color

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self):
        return f'Машина {self.name} развернулась'

    def show_speed(self):
        return print(f'Машина {self.name} имеет скорость: {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, color, name, speed, max_speed = 60):
        super().__init__(color, name, speed)
        self.max = max_speed


    def show_speed(self):
        if self.speed > self.max:
            return print(f'{self.color} {self.name} привышает скорость: {self.max} км/ч')

class WorkCar(Car):
    def __init__(self, color, name, speed, max_speed = 40):
        super().__init__(color, name, speed)
        self.max = max_speed


    def show_speed(self):
        if self.speed > self.max:
            return print(f'{self.color} {self.name} привышает скорость: {self.max} км/ч')

class SportCar(Car):
    def __init__(self, color, name, speed, min_speed = 130):
        super().__init__(color, name, speed)
        self.min = min_speed
        if self.speed > self.min:
            print(f'{self.color} {self.name} - спортивная. Ее тякущая скорость: {self.min} км/ч О_О')

class PoliceCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed)
        self.is_police = is_police
        if is_police:
            print(f'{self.color} {self.name} - полицейская, имеет особые привелегии.')

print('"Форсаж 20 - Python"')
town= TownCar('Audi','черная', 70)
work = WorkCar('Ford','белый', 70)
sport = SportCar('Lada','зеленая', 135)
police = PoliceCar('UAZ','фиолетовый', 70, True)
work.show_speed()
town.show_speed()
print(f'{police.go()}, соответственно {town.stop()}, {work.stop()}, а {sport.turn()}')


#5
class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")

class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")

print('"Канцтовары"')
pan = Pen()
pencil = Pencil()
handle = Handle()
pan.draw()
pencil.draw()
handle.draw()