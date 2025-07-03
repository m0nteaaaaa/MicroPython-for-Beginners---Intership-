#parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
   print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
#main start here

x = Person("Vijay", "Rahul") # x is an object of base class/ parent class Person 
x.printname()
#Child 
class Student(Person):
  pass

y = Student("Jio", "Virat")    # y is an object of child class
y.printname()

