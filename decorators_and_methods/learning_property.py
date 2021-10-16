""" @property decorator : Access a function of a class without the use of func() and just calling it by func
In short , it lets you treat a function like a variable of class 

Now the problem comes when you have to change the values of this variable dynamically .

That's whty we need property decorators (getter and setter)
Move to learning_property_decorators.py to learn more

"""

class Person:
    def __init__(self,first_name,last_name,company) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.email_id = self.email
        
    @property
    def email(self):
        return "{}_{}@{}.com".format(self.first_name,self.last_name,self.company)

a = Person("Ramamurthi","Gopalakrisnan","amazon")

# Storing the email
print(a.email)
print(a.email_id)

try :
    a.email = "rg@gmail.com"
except Exception as err:
    print(err)
print("You see the problem now?")