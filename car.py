class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print("Price:   "+str(self.price))
        print("Speed:   "+str(self.speed))
        print("Fuel:    "+str(self.fuel))
        print("Mileage: "+str(self.mileage))
        print("\n")

car1 = Car(12500, "95mph", "100%", 0)
car2 = Car(8600, "65mph", "100%", 18200)
car3 = Car(4400, "65mph", "70%", 54250)
car4 = Car(2150, "65mph", "40%", 103020)
car5 = Car(600, "65mph", "10%", 289490)