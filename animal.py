class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print(str(self.name)+" health: "+str(self.health) + "\n")
        return self

animal = Animal("Animal")
animal.walk().walk().walk().run().run().display_health()


class Dog(Animal):
    def __init__(self, name):
        super(self.__class__, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog = Dog("Bozo")
dog.walk().walk().walk().run().run().pet().display_health()


class Dragon(Animal):
    def __init__(self, name):
        super(self.__class__, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health += 10
        return self

    def display_health(self):
        print("This is dragon!")
        super(self.__class__, self).display_health()

dragon = Dragon("Smaug")
dragon.walk().walk().walk().run().run().fly().fly().display_health()
