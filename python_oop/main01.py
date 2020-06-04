class Car():
    wheel_count = 4
    

    def __init__(self, make_, model_, color, year):
        self.make = make_
        self.model = model_
        self.color = color
        self.year = year
        self.is_worked = False
        print('Masin yaradildi')

    def start(self):
        self.is_worked = True
        print(f'{self.make} ise dusdu')

    def move(self):
        if self.is_worked:
            print('masin hereket etdi')
        else:
            print('Zehmet olmasa masini ise salin!!')

car = Car('BMW', '750i', 'black', 1995)
car.start()
print('BMW Teker sayi', car.wheel_count)
car.wheel_count = 3
print('BMW Teker sayi', car.wheel_count)

car2 = Car('Audi', 'A5', 'red', 2020)
car2.start()
print('Audi Teker sayi', car2.wheel_count)




