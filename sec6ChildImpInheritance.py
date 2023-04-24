# inheritance is acquiring properties of parent class
# have access to all methods from parent to child
# if you have constructor which is not default,  make sure to call parent constructor into your child constructor

from sec6OopsDemo1 import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 4, 10)

    def getCompleteData(self):
        return ChildImpl.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())
