#Inheritance is where one class (child) acquires the properties and behaviors (variables 
# + methods) of another class (parent). 

# parent class  
class Employee:    
    start_time = "9AM"  
    end_time = "5PM"  
# child class  
class Teacher(Employee):  
    def __init__(self, subject):  
        self.subject = subject  
t1 = Teacher("Data Science")  
print(t1.subject, t1.start_time, t1.end_time) 

# 1.single inheritance: A child class inherits from a single parent class. In the example above, the Teacher class inherits from the Employee class.
class parent:
    def display(self):
        print("This is the parent class.")
class child(parent):
    def display2(self):
        print("This is the child class.")

c = child()
c.display()
c.display2()

#2. multiple inheritance: A child class inherits from multiple parent classes.

class Teacher:
    def __init__(self,salary):
        self.salary = salary
class Student():
    def __init__(self,gpa):
        self.gpa = gpa  

class TA(Teacher,Student):
    def __init__(self,name,salary,gpa):
        super().__init__(salary) #call parent constructor
        Student.__init__(self,gpa) #call parent constrcutot
        self.name = name

ta = TA("Rahul",50_000,7.5)
print(ta.name,ta.salary,ta.gpa)
# super() keyword - Used to call parent class’s method from child class.

#3.abstraction ->hiding unnecessary implementation details and showing only the 
# essential features to the user. 

#4.polymorphism
# -> ability of single function ,operator or object to behave diffrently based on context
# Same method name - works differently for different objects 
# Same operator - behaves differently depending on operand types 

print(1 + 2)  
# adds 2 numbers  
print("1" + "2") # concatenates 2 strings
#this called operator overloading

#2 types of polymorphism
#1.method overloading

class Animal:
    def sound(self):
        print("my name is animal")
class Cat(Animal):
    def sound(self):
        print("mai hu ogggy!! he he...")

a =Animal()
cat = Cat()
a.sound() #my name is animal
cat.sound() #mai hu ogggy!! he he... 

