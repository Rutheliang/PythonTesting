# in python, function is a group of related statements that perform a specific task
# function declaration

def Greet():
    print("Good Morning")
# function call
Greet()

def GreetMe(name):
    print("Good Morning "+name)
#parametize function / send parameters (string) from my function call
GreetMe("Ruthel")


def AddIntegers(a,b):
    print(a+b)


AddIntegers(2,3)


#you can also use return instead of print
def AddIntegers(c,d):
    return c+d

#return to AddIntegers the print (the same output)
print(AddIntegers(4,3))

