# classes are user defined blueprint or prototype
# example calculator -> methods/operations - sum, multiplication, addition, constant
# class will have methods, class variables, instance variables
# method & function are the same. called method if it's inside the class

class Calculator:
    num = 100 # class variables
    # default constructor

    def __init__(self): # constructor
        print("I an called automatically when object is created")

    def getData(self):
        print("I am now execution as method in class")


# you can call variable and method with an object
obj = Calculator() # syntax to create objects in python
obj.getData()
print(obj.num)



