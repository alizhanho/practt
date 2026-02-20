class Car:
    def __init__(self, brand, year):
        self.brand = brand  
        self.year = year

    def display_info(self):
        print(f"{self.brand}, {self.year}")


car1 = Car("Toyota", 2020)
car1.display_info()