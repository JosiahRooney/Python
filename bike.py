class Bike (object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def display_info(self):
        print("Price: " + str(self.price))
        print("Max Speed: " + str(self.max_speed))
        print("Miles: " + str(self.miles))
        return self

    def ride(self):
        print("Riding")
        self.miles += 10
        return self

    def reverse(self):
        print("Reversing")
        if self.miles > 5:
            self.miles -= 5
        else:
            print("Can't reverse!")
        return self

bike1 = Bike(200, "19mph")
bike1.ride().ride().ride().reverse().display_info()

print("\n")

bike2 = Bike(200, "19mph")
bike2.ride().ride().reverse().reverse().display_info()

print("\n")

bike3 = Bike(200, "10mph")
bike3.reverse().reverse().reverse().display_info()
