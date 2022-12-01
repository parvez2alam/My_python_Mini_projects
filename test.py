class Employee:
    def __init__(self,name, PerDaySal):
        self.name = name
        self.PerDaySal = PerDaySal



class Timesheet:
    def __init__(self,name,workingdays):
        self.workingdays = workingdays
    def __mul__(self, other):
        return other.PerDaySal*self.workingdays
e = Employee("parvez", 2580)
t = Timesheet("parvez",30)
print("Monthly salary for Parvez:",t*e)