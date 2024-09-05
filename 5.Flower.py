class Flower:
    def __init__(self,name,water_requirements):
        self.name = name 
        self.water_requirements = water_requirements
        self.is_happy = False
    def water(self,quantity):
        if quantity == self.water_requirements:
            self.is_happy = True
        else:
            self.is_happy = False
    def status(self):
        if self.is_happy:
            print(self.name + ' is happy')
        else:
            print(self.name + ' is not happy')
flower = Flower("Lilly", 100)
flower.water(50)
flower.status()
flower.water(100)
flower.status()
