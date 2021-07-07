# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
# 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
from sys import argv

#script, a = argv - раскоментить, чтобы принимать значение из командной строки

a = 1 #int(a) - раскоментить и удалить '1' чтобы принимать значение из терминала

class TrafficLight:
    
    __color = ['Red', 'Yellow', 'Green']
    
    def running(a):
        for i in range(a):
            print(TrafficLight.__color[i%3])
            if TrafficLight.__color[i%3] == 'Red':
                time.sleep(7)
            elif TrafficLight.__color[i%3] == 'Yellow':
                time.sleep(2)
            else:
                time.sleep(5)
                
TrafficLight.running(a)
print('\n')


#Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
#Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
#Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
#Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. 
#Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т

from sys import argv

#script, a, b = argv

a = 1
b = 1

class Road:

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)
        
    def asphalt_amount(self):
        return self._length * self._width * 25 * 5
        
road1 = Road(a, b)
print(road1.asphalt_amount())
print('\n')


#Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
#Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
#Создать класс Position (должность) на базе класса Worker. 
#В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
#Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

honey_money = {'Laborer': {'wage': 1, 'bonus': 1},
                'Woodcutter': {'wage': 2, 'bonus': 2},
                'Scavenger': {'wage': 3, 'bonus': 3},
                'Miner': {'wage': 4, 'bonus': 4}}

class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = honey_money[position]['wage'] + honey_money[position]['bonus']
        
class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        
    def get_full_name(self):
        return f'{self.name} {self.surname}'
        
    def get_total_income(self):
        return self._income
        
a = Position('Rudy', 'Rubby', 'Laborer')
b = Position('Bob', 'Minion', 'Scavenger')

print(a.get_full_name())
print(a.get_total_income())
print(b.get_full_name())
print(b.get_total_income())
print('\n')


#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
#А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
#Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
#Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color = 'Цвет ржавчины', name = 'Ведро с болтами'):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        
    def show_speed(self):
        return f'{self.name} несется со скоростью {self.speed}'
        
    def go(self):
        return 'Машина поехала'
        
    def stop(self):
        return 'Машина остановилась'
        
    def turn(self, direction):
        return f'Машина повернула на {direction}'
        
class TownCar(Car):

    def __init__(self,  speed, color = 'Цвет ржавчины', name = 'Ведро с болтами'):
        super().__init__(speed, color, name)
        
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости! Остановите {self.name}'
        else:
            return super().show_speed()
            
class WorkCar(Car):

    def __init__(self,  speed, color = 'Цвет ржавчины', name = 'Ведро с болтами'):
        super().__init__(speed, color, name)
        
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости! Остановите {self.name}'
        else:
            return super().show_speed()
            
class SportCar(Car):

    def __init__(self,  speed, color = 'Цвет ржавчины', name = 'Ведро с болтами'):
        super().__init__(speed, color, name)
        
            
class PoliceCar(Car):

    def __init__(self,  speed, color = 'Цвет ржавчины', name = 'Ведро с болтами'):
        super().__init__(speed, color, name)
        self.is_police = True

a = PoliceCar(60, 'blue', 'Mazda')
b = SportCar(120, 'red', 'Запорожец')
c = WorkCar(50, 'Yellow', 'BMW')
d = TownCar(speed = 40)

print(d.show_speed())
print(a.go())
print(b.stop())
print(c.turn('право'))
print(a.is_police)
print(a.show_speed())
print(b.show_speed())
print('\n')


#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). 
#Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
#В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
#Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title
        
    def draw(self):
        print('Запуск отрисовки.')

        
class Pen(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
        
    def draw(self):
        super().draw()
        print(f'Эти каракули нарисованы {self.title}.\n')

        
class Pencil(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
        
    def draw(self):
        super().draw()
        print(f'Что за серость? Это что, {self.title}?\n')

        
class Handle(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
        
    def draw(self):
        super().draw()
        print(f'Эту жирную линию оставил {self.title}.\n')


a = Pen('Биг')
b = Pencil('Кух-и-Нур')
c = Handle('Просто маркер')

a.draw()
b.draw()
c.draw()