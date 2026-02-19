#inheriance 


#Multiple inheritance: inherit from more than one parent class C(A,B)
#mutilever inher: inherit from a parent which inherits from another parent c(B) <-B(A) <- A

class Animal:
    def __init__(self, name:str) -> None:
        self.name=name

    def eat(self):
        print(f'{self.name} is eating')

class Pray(Animal):
    def eaten(self):
        print('I am pray') 
class Pradator(Animal):
    def eat(self):
        print('I will eat other pray')  
class Fist(Pray, Pradator):
    pass






#Absract class : A class that cannot be instantiated on its own; Meant to be subclassed.
#                   They can contain abstract methods , which are declared but have no implementation.
#                   Abstract classes benefits:
#                    1. Prevents instantiation of the class itself
#                   2. requres children to use inherited abstract method


from abc import ABC, abstractmethod


class Vechicle(ABC):

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vechicle):
    def go(self):
        print("i am going")

    def stop(self):
        print('I am stopped')


#super()= Fuction used in a child class to call methods from a parent class (superclass).
#            allow you to extend the functionality of the inherited methods


class Shape:
    def __init__(self, color:str, is_filled:bool):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print('I am main class')
    
class CircleShape(Shape):
    def __init__(self,color:str, is_filled:bool,radius:float):
        super().__init__(color:str, is_filled:bool)
        self.radius = radius
    
    def describe(self):
        print(super().describe()) 
        print('I am from the circle shape')


#Polymorphism = Many faces
 # two ways to achieve polymorphism
#Inheritance
#Duck typing



#Aggregation = Represents a relationship where one object (the whole)
                #contains references to one or more INDEPENDENT objects (the parts)


class Library:
    pass

class Book:
    pass


#composition = the composed object directly owns its components, which cannot exist independently
#  "owns-a" relation


class Engine:
    def __init__(self,horse_power):
        self.horser_power = horse_power


class Wheel:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self):
        self.engine = Engine(430)
        self.wheel = Wheel(3)


a = ("1","2")
print(a.join(","))

tuple
#static mehtod

#class method

#instance metod



