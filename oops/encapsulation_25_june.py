"""Encapsulation is one of the fundamental principles of object-oriented 
programming (OOP) that bundles the data (attributes) and methods (functions)
that operate on the data into a single unit called a class. The key idea
behind encapsulation is to hide the internal state and implementation details
of an object from the outside world and only expose a controlled interface
to interact with the object"""
#####
# Public attributes/methods: Accessible from outside the class.
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

    def reset_pass(self, new_pass):
        self.new_pass = new_pass
        print("new password", self.new_pass)

acc1 = Account(12345, "abcde")
print(acc1.acc_no)
print(acc1.acc_pass)

acc1.reset_pass("qwert")
print(acc1.new_pass)

#####
# Private attributes/methods: Accessed only from within the class
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print("can you reset this password", self.__acc_pass)
        
    
acc1 = Account(12345, "abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass)  can't access out side the class

print(acc1.reset_pass())


# private method
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        self.__new_pass()
        # print("can you reset this password", self.new_pass)

    def __new_pass(self):
        self.new_pass = "harsh"
        print("new_pass is", self.new_pass)


class Manger(Account):
    def display(self):
        print("acc_no: ", self.acc_no)
        # print("self acc_pass: ", self.__acc_pass) # can't access outside the class
    
    
acc1 = Manger(12345, "abcde")
acc1.display()
# acc1.__new_pass   we can't access out side the class
acc1.reset_pass()



