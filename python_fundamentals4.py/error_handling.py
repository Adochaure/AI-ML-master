#an exception is an error that occus while program is runnnig ,if not handled, program crashes

# ex> dividing by 0 -> ZeroDivisionError
#using an undefined variable - NameError
#Opening a missing file - FileNotFoundError
#Wrong data type -> TypeError

try:
    #code to execute
    x = 10 / 0  
except:
    #code to execute
    print("Error happend!")

#also throw specific exceptions
try:
    print(10/0)
except ZeroDivisionError:
    print("You can not divide by zero!")


#else block -> executes only if no exception happens.
# try:  
#     x = int(input("Enter a number: "))  
# except ValueError:  
#     print("Invalid input!")  
# else:  
#     print("You entered:", x) 

#finally block -> always executes -. its for clean up task like closing files and relesing resources
try:
    with open("data.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File Not Found.")
finally:
    print("Execution Completed.")


