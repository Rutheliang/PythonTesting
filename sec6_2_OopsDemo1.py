#  self keyword is mandatory for calling variable names into method / self is default added in method
#  instance and class variable have whole different purpose / one is attach to object (instance) and other is not
# class variable (constant) created inside class / instance variable define inside method
# constructor name should be __init__
# init is the keyword in creating constructor
#  new keyword (java is using new keyword) is not required when you create object
#  from FunctionsDemo import GreetMe, AddIntegers
# default constructor created if no define in the class


class Calculator:
    num = 100 # class variables / not change
    # default constructor if not created
    # constructor called first

    def __init__(self, a, b):  # constructor
        self.firstNumber = a  # instance variable (value is changing depends on object creation) / stored
        self.secondNumber = b

        print("I an called automatically when object is created")

    def getData(self):
        print("I am now execution as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num
        # you can never call any variable with its name / always attached "self"
        # self is universal or global to call any constant and instance variables / you can use also Calculator.num
        # in python always attached "self"
        # call any variable inside of method, you have always call that variable with self


obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())


