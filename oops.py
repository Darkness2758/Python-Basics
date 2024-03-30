class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def getSalary(self):
        return self.salary
    
rohan = Employee("Rohan", "20000000")
print(rohan.salary)
print(rohan.name)