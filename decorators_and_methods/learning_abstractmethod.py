""" abstractmethod : Creates a structure for the child class and if you try to invoke a function in child class which is not present in the child class but is present in the abstract class , 
you can send a message through the parent class using NotImplementedError using the @abstractmethod . 
You can also check the inheritance using issubclass() function """

from abc import (
    ABC,
    abstractmethod,
)


class Parent:
    count = 0

    def __init__(
        self,
    ) -> None:
        pass

    @abstractmethod
    def f1(self, **kwargs):
        print("f1 parent invoked")
        raise NotImplementedError("Child must implement f1 method!")

    @abstractmethod
    def f2(self, **kwargs):
        print("f2 parent invoked")
        raise NotImplementedError("Child must implement f2 method!")

    @abstractmethod
    def f3(self, **kwargs):
        print("f3 parent invoked")
        raise NotImplementedError("Child must implement f3 method!")

    @abstractmethod
    def f4(self, **kwargs):
        print("f4 parent invoked")
        raise NotImplementedError("Child must implement f4 method!")

    @abstractmethod
    def f5(self, **kwargs):
        print("f5 parent invoked")
        raise NotImplementedError("Child must implement f5 method!")

    # @classmethod
    # def add_counter(cls):
    #     cls.count+=1
    #     print("Counter Added")

    # @classmethod
    # def return_counter(cls):
    #     print("Counter Added")
    #     return cls.count


class Child(Parent):
    # pass
    def f1(self, **kwargs):
        print("f1 child invoked")

    def f2(self, **kwargs):
        print("f2 child invoked")

    def f3(self, **kwargs):
        print("f3 child invoked")

    def f4(self, **kwargs):
        print("f4 child invoked")

    # def f5(self,**kwargs):
    #     print("f5 child invoked")


parent = Parent()
child = Child()
child.f5()
print(issubclass(Child, Parent))
print(isinstance(Child(), Parent))
