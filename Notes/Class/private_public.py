class MyClass:
    def __init__(self, name):
        # Public member
        self.name = name
         # Private member (name mangling)
        self.__age = 0
        # Public method to set the age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
# Public method to get the age
    def get_age(self):
        return self.__age  
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.__age}")
    
 #main
# Create an instance of MyClass
obj = MyClass("John")
# Access public member 'name'
print(obj.name)  # Output: John
# Access private member 'age' using a public method
obj.set_age(30)
# Access private member 'age' using a public method
print(obj.get_age())  # Output: 30

# Access private member '__age' directly (name mangling)
# Note that this is possible but discouraged
print(obj._MyClass__age)  # Output: 30

# Call a public method to display information
obj.display_info()
