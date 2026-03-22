class Car:
    total_cars = 0
    def __init__(self, brand:str, speed: int = 0):
        self.brand = brand
        self.speed = speed
        self._fuel =100
        self.__engine_id = "S123"
        Car.total_cars += 1

    def __repr__(self):
        return f"Car(brand='{self.brand}', speed = '{self.speed}'"
#   Instance method
    def accelerate(self, amount:int):
        self.speed += amount
        self._fuel -=amount*0.5
        return self

    def __del__(self):
        Car.total_cars -= 1

car = Car("Tesla", 0)
car.accelerate(10).accelerate(50)
print(car)