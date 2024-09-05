class Hero:
    def __init__(self,name,health):
        self.name = name 
        self.health = health
    def defend(self,damage):
        self.health = self.health - damage
        self.check_heal()
    def heal(self,heal):
        self.health = self.health + heal
        self.check_heal()
    def check_heal(self):
        if self.health == 0:
            print(self.name + ' was defeated')
        else:
            print('None')
tung = Hero("Tung",100)
tung.defend(50)
tung.heal(10)
tung.defend(60)
