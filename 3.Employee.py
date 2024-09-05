class Employee:
    def __init__(self,id,first_name,last_name,salary):
        self.id = id 
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def get_full_name(self):
        print(self.first_name +' '+ self.last_name)
    def get_annual_salary(self):
        self.annual_salary = self.salary * 12 
        print('Your salary in 12 months is ' +str(self.annual_salary))
    def raise_salary(self,amount):
        self.salary = self.salary + amount
        print('Your Salary was increased to ' +str(self.salary))
tung = Employee("23011402","Thanh","Tung",5000)
tung.get_full_name()
tung.get_annual_salary()
tung.raise_salary(5000)
tung.get_annual_salary()

