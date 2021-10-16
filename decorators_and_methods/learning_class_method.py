""" 
classmethod : is a function used to call the attribute of the class and not the object of a class . 
Used usually to store/edit class related information
You don't need to pass self as an argument here .

"""


from abc import ABC,abstractmethod

class Parent:
    
    count = 0
    
    def __init__(self) -> None:
        Parent.add_counter()
        self.instance_no = Parent.return_counter()    
    
    @classmethod
    def add_counter(cls):
        cls.count+=1
        print("Counter Added")
    
    @classmethod
    def return_counter(cls):
        return cls.count

parent1 = Parent()
parent2 = Parent()
parent3 = Parent()

for i in [parent1,parent2,parent3]:
    
    print("instance_no" , i.instance_no)