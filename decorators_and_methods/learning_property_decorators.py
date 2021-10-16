""" 
@property decorator : Access a function of a class without the use of func() and just calling it by func
In short , it lets you treat a function like a variable of class with the name same as function

Now the problem comes when you have to change the values of this variable dynamically .

That's why we need property decorators (getter and setter)
Move to learning_property_decorators.py to learn more

Three main important functions are assoiciated with the @property decorator
 - Setter
 - Deleter
 - Getter

So email now is dependent on first name and last name here . If you want to upate email directly , you also need to update first name and last name 
in such a way that the relationship of the email never breaks 

""firstname_lastname@company.com"" will always be the format of the email and there is no exception to this .
However you can also change the first name and last name based on the email given to you 

for example : 
    firstname = Pete
    lastName = Holmes
    comapny = amazon
    email = Pete_Holmes@amazon.com

if we want to change this variable to 
    email = Jermy_Howard@fastai.com
All the other variables firstname,lastname and comapny should get updated accordingly in such a way that the @property function never breaks at any point
    firstname = Jermy
    lastName = Howard
    comapny = fastai
    email = Jermy_Howard@fastai.com

This is where we use the setter 



@setter : setter gets called when you assign a value to the variable assigned with @property decorater . It takes inputs as the value assigned to it 
and the function definition is completely upto us to work on . 

Note : Can be anything . In the end , it is not required that the property ends up with the value assigned to it .the property variable is always calculated using the parameters of the class 


@getter :



"""

class Person:
    def __init__(self,first_name,last_name,company) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        
    @property
    def email(self):
        return "{}_{}@{}.com".format(self.first_name,self.last_name,self.company)

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
    
    def print_person_details(self):
        print("First name :", self.first_name)
        print("Last name :",self.last_name)
        print("Company name :",self.company)
        print("EmailID :",self.email)




person = Person("Pete","Holmes","amazon")

# Storing the email
person.print_person_details()
person.email = "Jermy_Howard@fastai.com"
print(person.print_person_details())

del person.email
print(person.print_person_details())