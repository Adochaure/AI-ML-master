#conditional statements

#ex1
x=10
if x>5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

#ex2
color = "orange"  
if color == "red":  
    print("Stop")  
elif color == "yellow":  
    print("Look")  
elif color == "green":  
    print("Go")  
else:  
    print("wrong color")

#Ternary Statement
age = 20
status = "Adult" if age>22 else "baburao"
print(status)

#Match case statement -> alternative to if-elif-else statement
day = "Monday"

match day:
    case "Monday":
        print("Today is Monday")
    case "Tuesday":
        print("Today is Tuesday")
    case "Wednesday":
        print("Today is Wednesday")
    case "Thursday":
        print("Today is Thursday")
    case "Friday":
        print("Today is Friday")
    case "Saturday":
        print("Today is Saturday")
    case "Sunday":
        print("Today is Sunday")
    case _:
        print("Invalid day")


#Loops

#1.while loop

i=1
while(i<5):
    print(i+1)
    i+=1

#break -> it stops loop imediately when condition is met
for i in range(1, 6):
    if i == 3:
        break
    print(i)

j=0
#continue -> it skips the current iteration and continues with the next iteration
for j in range(1, 6):
    if j == 3:
        continue
    print(j)

#For loop 
for i in range(1,3):
    print(i)

# in keyword -> it is used to check if a value exists in a sequence (list, tuple, string etc.)
word = "artificial intelligence"  
count = 0  
for ch in word:  
    if ch == 'i':  
        count += 1  
print(f"i occurs {count} times.")



#FUnctions
def hello():
    print("hass re halkat hass!")

hello()  # calling the function


#2
#  Fnx to computer average of 3 nums  
def avg(a, b, c):  
    return (a + b + c) / 3  
print(avg(1, 2, 3))  # Output: 2.0


#Lambda function -> it is a small anonymous function that can take any number of arguments, but can only have one expression. It is often used when you need a simple function for a short period of time.
square = lambda x: x ** 2
# syntax: lambda arguments: expression    
print(square(5))  # Output: 25 