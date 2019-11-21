#10/31/2019 Valarie Harrison
class Employee:
    #Common base class for all employees
    empCount = 0
    empYear = 2001

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary : ", self.salary

emp1 = Employee("Kwon",300)
emp2 = Employee("Larsen",1000)
emp3 = Employee("Com",3500)

print emp1.displayCount()
print emp2.displayEmployee()
emp1.name = "Hill"
emp1.displayEmployee()

#Cars

class Cars:
    year = ""
    model = ""
    def __init__(self,owner):
       self.owner = owner
    def value(self):
        print self.owner, "'s car value is $",self.year * 10

car1 = Cars("Kwon")
car1.year = 2019
car1.value()
car2 = Cars("Cox")
car2.year = 1995
car2.value()
