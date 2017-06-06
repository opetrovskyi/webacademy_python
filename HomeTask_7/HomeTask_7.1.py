# 1.0 Создать класс Автомобиль содержащий информацию: модель, цвет, год_выпуска, стоимость. Описать метод __str__.
# Пример
# >> car1 = Car(‘Audi’, ‘Red’, ‘1999’, ‘$12000’)
# >>print(car1)
# name: Audi
# color: Red
# year: 1999
# price: $12000


class Transport:
    def __init__(self, color, year, price):
        self.color = color
        self.year = year
        self.price = price

class Car(Transport):
    def __init__(self, model, color, year, price):
        super().__init__(color, year, price)
        self.model = model

    def __str__(self):
        return 'name: {}\ncolor: {}\nyear: {}\nprice:{}'.format(self.model, self.color, self.year, self.price)


class Moto(Transport):
    pass


car1 = Car('Audi', 'Red', '1999', '$12000')

print(car1)