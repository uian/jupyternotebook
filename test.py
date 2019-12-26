#!/usr/bin/python
class Employee (object):
  empCount = 0
 
  def __init__(self, name, salary) :
    self.name  = name
    self.salary = salary
    Employee.empCount += 1
 
  def displayCount(self) :    
    print "total employee ",Employee.empCount
 
  def displayEmployee(self) :
    print "name :",self.name  , ", salary :", self.salary
 
emp1 = Employee("SR", 10000)
emp1.displayCount()
emp1.displayEmployee()
emp1.salary = 20000  
print emp1.salary
emp1.age = 25  
print emp1.age
del emp1.age
 
Employee.empCount=500
print Employee.empCount
 
Employee.cc="abc"
print Employee.cc
 
del Employee.empCount
 
