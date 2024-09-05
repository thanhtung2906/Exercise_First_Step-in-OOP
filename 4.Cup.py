class Cup:
    def __init__(self,size,number):
        self.size = size 
        self.number = number 
    def fill(self,milliliters):
        if self.number == self.size:
            print('Cupp is full!')
        else:
            self.number = self.number + milliliters
            print(self.number)
    def status(self):
        self.free = self.size - self.number
        print(self.free) 
cup = Cup(100,50)
cup.status()
cup.fill(100)
    