#parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
   print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Vijay", "Rahul")  # x is an object of base class
x.printname()
#Child 
class Student(Person):
 def __init__(self, fname, lname):
   self.firstname = fname
   self.lastname = lname
 def printfname(self):
   print(self.firstname)
 def printlname(self):
   print(self.lastname)

y = Student("Jio", "Virat") # y is an object of child class
y.printname() # y is accessing method from basecalss
y.printfname()  # this is a method from child class
y.printlname()  # this is  method from child class

