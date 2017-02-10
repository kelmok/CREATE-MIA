class Employee:

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def displayEmployee(self):
    print "Name: ", self.name,  ", Salary: ", self.salary

class RemoteEmployee(Employee):

  def __init__(self, name, salary, location):
    Employee.__init__(self, name, salary)
    self.location = location

  def displayEmployee(self):
    Employee.displayEmployee(self)
    print "Location: ", self.location

