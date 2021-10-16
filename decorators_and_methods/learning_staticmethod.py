""" 
When you have a bunch of functions and you want give them a stucture and to add them to a class but you don't want to use an object to use them . 
Main difference between classmethod and staticmethod is that the class method takes in the arg as Class and has access to class variables (not object variables)
and the staticmethod only us access to that particular function and none of the class variables

"""

class Math:
    
    def __init__(self) -> None:
        pass
    @staticmethod
    def simple_add(a,b):
        return a+b
    
    @staticmethod
    def simple_sub(a,b):
        return a-b
    
print(Math.simple_add(1,2))
print(Math.simple_sub(1,2))
       