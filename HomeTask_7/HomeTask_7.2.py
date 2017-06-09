# 1.1 Создать класс Автосалон содержащий информацию: адрес, имя, список доступных машин.
# Реализовать методы для отображения всех доступных машин, добавления новых машин, покупки машин (после покупки машина удаляется из списка) + проверки на наличие такой машины в салоне
# Пример
# >> car1 = Car(‘Audi’, ‘Red’, ‘1999’, ‘$12000’)
# >> car2 = Car(‘BMW’, ‘Black’, ‘2009’, ‘$18000’)
# >>
# >>showroom = ShowRoom(‘Borshagovska 17’, ‘Volkswagen showroom’)
# >>showroom.add_car(car1)
# >>showroom.add_car(car2)
# >>
# >>showroom.show_all()
# 1
# ————————-
# name: Audi
# color: Red
# year: 1999
# price: $12000
#
# 2
# —————————
# name: BMW
# color: Black
# year: 2009
# price: $18000
# >>showroom.sell_car(Car(‘Volvo’, ‘Red’, ’1993’, ‘$20000’))
# ‘No such car!’
# >>showroom.sell_car(car1)
# ‘Car has been sold!’
# >>showroom.show_all()
# 1
# —————————
# name: BMW
# color: Black
# year: 2009
# price: $18000
#


class Car:
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return 'name: {}\ncolor: {}\nyear: {}\nprice: {}\n'.format(self.model, self.color, self.year, self.price)

    def __repr__(self):
        return str(self)


class ShowRoom:
    def __init__(self, addres, name):
        self.addres = addres
        self.name = name
        self._cars = []

    def add_car(self, car):
        self.car = car
        self._cars.append(car)
        return print("Done")

    def sell_car(self, car):
        self.car = car
        if car in self._cars:
            self._cars.remove(car)
            return 'Car has been sold!'
        else:
            return 'No such car!'

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'adress: {}\nname: {}\n'.format(self.addres, self.name)

    def show_all(self):
        return print(*self._cars, sep='\n')

car1 = Car('Audi', 'Red', '1999', '$12000')
car2 = Car('BMW', 'Black', '2009', '$18000')
car3 = Car('Volvo', 'Black', '1199', '$1800000')
showroom = ShowRoom('Borshagovska 17', 'Volkswagen showroom')
showroom2 = ShowRoom('Lala str 17', 'Popovoz showroom')
showroom2.add_car(car1)
showroom2.add_car(car2)

showroom.add_car(car1)
showroom.add_car(car3)



print('*' * 55)
print(showroom.show_all())
print('*' * 88)
print(showroom2.show_all())
print('*' * 88)
print(showroom.sell_car(car1))
print('*' * 55)
print(showroom.sell_car(Car('Audi', 'Red', '1999', '$12000')))
print('*' * 88)
print(showroom)
print('*' * 55)
showroom.show_all()
print('*' * 88)
print(showroom2)
print('*' * 88)
showroom2.show_all()


