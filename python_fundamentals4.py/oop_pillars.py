# 4 key pillars of OOP
#1.Encapsulation 
#2.Abstraction
#3.Inheritance
#4.Polymorphism

#1.Encapsulation ->  to protect the data from accidental or unauthorized modification. 


#Public variable -> Accessible everywhere
#. Protected members->indiacted by _ ->Still accessible from outside (not truly protected). 
#Private variable -> by __ ->
class Student:
    def __init__(self,name,balance):
        self.name = name  #public variable
        self._age = 20 #Protected variable
        self.__balance = balance #private
s = Student("Raju",55000)
print(s.name)
print(s._age)
print(s._Student__balance)


#Getter and seteer methods -> used to access private variable
class Employee:  
    def __init__(self, salary):  
        self.__salary = salary  # private 
    def get_salary(self):    
        return self.__salary    # getter 
    def set_salary(self, new_salary):  
        self.__salary = new_salary  # setter  
e = Employee(50000)  
print(e.get_salary())  #50000
e.set_salary(60000) 
print(e.get_salary())  #60000

