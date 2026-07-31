# Object Oriented Programming in Python
#  It helps us structure programs in a way that is modular, reusable, and 
# easier to maintain. 

# class -> blueprint of creating object
# it describes what an object will look like (its attributes) and what it can do (its 
# methods), but it is not the object itself.

#ex1>
class Car:  
    brand = "Toyota"

#Object : object is realization of class , thing that actual build on template of class

car1 = Car()
car2 = Car()
print(car1.brand)
print(car2.brand)

#Attributes-> are variables And Method are-> functions defined inside class


#Constructor in OOP -> sepcial method used to initalze newly created object ->set up onject with inital value

# syntax
class Student:
    def __init__(self):
        print("Constructor was called")
stu1 = Student() # "constructor was called" 

#self -> instance of class
class Students:  
    def __init__(self, name):  
        self.name = name  
stu3 = Students("Aditya")  
stu2 = Students("Chaure 01")  
print(stu3.name, stu2.name) # Rahul Harshita  

#types of constructors -> 1. default(no parameter except self)  2.parameterized(takes parameter)

#Attributes are variables that belong to a class or an object. 

#Types 1. class attribute
#- belong to class itself , shared by all object
#-defined outside any method in the class
class Student:  
    college = "ABC college"   
stu1 = Student ()  
# class attribute  
print(stu1.college)  
print(Student.college) # class attribute can also be accessed with class name

#type 2: instance attr
# belogn individual to each object
class Stud:  
    def __init__ (self, name, gpa): # instance attributes  
        self.name = name  
        self.gpa = gpa  
stu420 = Stud("Rahul", 8.7)  
print(stu420.name, stu420.gpa) 


#Method in python -> functions defined inside class

# 1.Instance Method
# -> take self as first argument
#-> can access both instace and class attribute

# class Student24:  
#     def   init  (self, name, marks):  
#         self.name = name  
#         self. marks = marks  
#     def display(self):   # Instance method  
#         print(f"Name: {self.name}, Marks: {self.marks}") 

#2.class Methods
# use @classmethod
# take cls as first argument -> used to work with class level data
class Road:
    road_name = "teda meda rasta"

    @classmethod
    def change_road(cls,new_road):
        cls.road_name = new_road

r1 = Road()
r1.change_road("sidhaa rast")
print(r1.road_name)

#3.static methods -> @staticmethod -> not take self or cls ->behave like normal func but be;logn to class for locgic gruoping
class math:
    @staticmethod
    def add(a,b):
        return a*b

m1 = math()
print(m1.add(3,4))
