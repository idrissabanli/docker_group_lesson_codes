class Car():
    wheel_count = 4
    yanacaq_sefiyyati = 10 # 100km-e 1 litr

    def __init__(self, make_, model_, color, year, fuel_amount):
        self.make = make_
        self.model = model_
        self.color = color
        self.year = year
        self.is_worked = False
        self.fuel_amount = fuel_amount
        print(f'{self.make} yaradildi')

    def start(self):
        self.is_worked = True
        print(f'{self.make} ise dusdu')

    def move(self, distance):
        if self.is_worked:
            self.fuel_amount -= distance * self.yanacaq_sefiyyati/100
            if self.fuel_amount < 0:
                print(f'{self.make} {distance}km hereket ede bilmedi. Cunki yanacagi kifayet etmir!')
                self.fuel_amount = 0
                self.stop()
                return
            print(f'{self.make} {distance}km hereket etdi')
            print(f'qalan yanacaq {self.fuel_amount} l')
        else:
            print(f'Zehmet olmasa {self.make}-ni ise salin!!')

    def stop(self):
        self.is_worked = False
        print(f'{self.make} dayandi')

class Sedan():
    door_count = 4

    def start(self):
        print('Sedan start methodudur')

class BMW(Car, Sedan):
    yanacaq_sefiyyati = 100000

    def start(self):
        print(f'Bura bmw-nin start methodudur')
        super(BMW, self).start()
    
    def drift(self):
        if self.is_worked:
            print(f'{self.make} drift etdi')
        else:
            print('Bmw-ni ise salin')
        

bmw = BMW('BMW', '750i', 'black', 1995, 30)
bmw.start()
bmw.move(10)
print(bmw.door_count)
# bmw.move(100)
# bmw.move(300)
# bmw.drift()
# bmw.start()
# bmw.drift()

# car = Car('BMW', '750i', 'black', 1995, 30)
# car.start()
# car.move(10)
# car.move(100)
# car.move(300)


# car2 = Car('Audi', 'A5', 'red', 2020, 40)
# car2.move(5)






