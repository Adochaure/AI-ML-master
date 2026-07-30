# a data type is kind value a variable can hold

x = 10  
print(type(x))         # <class 'int'> 

PI = 3.14  
print(type(PI))        # <class 'float'> 

name = "shradha"  
print(type(name))     # <class 'str'>  

isTeacher = True  
print(type(isTeacher))  # <class 'bool'> 

empty_var = None  
print(type(empty_var))  # <class 'NoneType'> 


#Type Conversion & Type Casting 

# 1.type conversion

a = 6
b = 3.0
ans = a+b
print(type(ans))    #<class 'float'>
print(ans)          # 9.0

# 2.type Casting

y = float(a)
z = str(a)
print(type(z))      #<class 'str'



#int() 
# ,                
# float() 
# ,       
# str() 
# ,          
# bool() 
# ,           
# list() 
# ,              
# tuple() 
# are common type conversion


#Operator - tell python to perform specific computaion

print(1+4)  # "+" is a operator & (1,3) are operand

#1.Arithmetic Operator
#  + ,- ,*,/,%,**

a = 5  
b = 10  
print(a + b) 
print(a - b)  
print(a * b)  
print(a / b)  
print(a % b)  
print(a ** b)

#Relational operator - used to compare values

#Operator  :-> == , != , > , >= , < , <=


#Logical Operator

#ex> and , or , not()

#Left shift and right shift operator

a = 10
print(a << 2)  # left shift operator * 2^n
print(a >> 2)  # right shift operator / 2^n


#input() - used to take input from user

name = input("Enter your name:" )
print(name)