""" Making use of all the learning under the module decorators_and_methods """

from abc import abstractmethod

def print_pretty(func):
    def wrapper(*args,**kwargs):
        print("*"*50)
        func(*args,**kwargs)
        print("*"*50)
        
    return wrapper

class Template:

    @property
    def fullname(self, *args , **kwargs):
        raise NotImplementedError(" fullname Method has not been implemented")
    
    @abstractmethod
    def return_total_class_vars(self, *args , **kwargs):
        raise NotImplementedError(" return_total_class_vars Method has not been implemented")
    


class Person(Template):
    
    count = 0

    def __init__(self,first_name,last_name,company) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.email_id = self.email
        Person.counter()

    
    @property
    def email(self):
        return "{}_{}@{}.com".format(self.first_name,self.last_name,self.company)
    
    @email.setter
    def email(self,email_id):
        first_name , _last_name = email_id.split('_')
        last_name , _comapny = _last_name.split('@')
        company , _domain = _comapny.split('.')

        self.first_name = first_name
        self.last_name = last_name
        self.company = company 
    
    @email.deleter
    def email(self):
        
        self.first_name = None
        self.last_name = None
        self.company = None
    
    @classmethod
    def counter(cls):
        cls.count+=1
    
    # @print_pretty not possible here since it can only be applied on functions and not static method objects
    @staticmethod
    def description():
        print("The class contains details about names company and email_ids of different persons")
    
    @print_pretty
    def class_name(self):
        print(Person.__name__)
    
    @print_pretty
    def instance_name(self):
        print(self.__name__)
    

    
    
if __name__ == "__main__":
    
    per = Person("Ramamurthi","Gopalakrisnan","amazon")

    # Check @Property
    print("Email_ID :",per.email)    

    #  @classmethod functionality
    print(" No of classes ",Person.count)    

    #  @staticmethod functionality and decorator's functionality
    print(" Description of class : ") 
    Person.description()   

    #  @decorator functionality
    per.class_name()
    
    #  abstractmethod property functionality
    try :
        per.fullname
    except Exception as err:
        print(err)
    
    #  abstractmethod function functionality
    try :
        per.return_total_class_vars()
    except Exception as err:
        print(err)
    