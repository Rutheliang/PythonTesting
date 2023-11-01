# inheritance is acquiring properties of parent class
# have access to all methods from parent to child
# if you have constructor which is not default,  make sure to call parent constructor into your child constructor

from sec6_2_OopsDemo1 import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 4, 10)
        # if you have constructor which is not default in parent,  make sure to call parent constructor into your child constructor

    def getCompleteData(self):
        return ChildImpl.num2 + self.num + self.Summation()
        # num2 = 200
        # num  = 100
        # summation = 4+10+100 = 114
        # total = 414


obj = ChildImpl()
print(obj.getCompleteData())
