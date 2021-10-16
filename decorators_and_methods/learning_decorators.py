""" 

    Decorators - Used in places where there's generally a repeated block of code in every function that can be common . 
    It takes in the arg as function and returns another function. 
    It's generally a wrapper function 

"""
import time

def decorator_function(func):
    def wrapper(*args,**kwargs):
        
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        
        print(func.__name__ ," took " , (end-start)*1000 , "mil seconds")
        
        return result 
    return wrapper

@decorator_function
def divide_nums(a,b):
    print(a/b) 


divide_nums(9,2)