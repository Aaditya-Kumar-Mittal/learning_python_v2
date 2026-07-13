class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}")
    
    @staticmethod
    def car_greeting():
        print("Welcome to the car showroom!")
        
    @staticmethod
    def start_engine():
        print("The engine has started.")
    
    @staticmethod
    def test_drive():
        print("The car is ready for a test drive.")
    
    @staticmethod
    def car_farewell():
        print("Thank you for visiting the car showroom!")

class Toyota(Car):
    def __init__(self, model, year):
        super().__init__("Toyota", model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")

class Lexus(Car):
    def __init__(self, model, year):
        super().__init__("Lexus", model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")

class Maserati(Car):
    def __init__(self, model, year):
        super().__init__("Maserati", model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")

toyota_car = Toyota("Camry", 2022)
lexus_car = Lexus("RX", 2021)
maserati_car = Maserati("Ghibli", 2023)

toyota_car.display_info()
lexus_car.display_info()
maserati_car.display_info()

toyota_car.car_greeting()
toyota_car.start_engine()
toyota_car.test_drive()
toyota_car.car_farewell()