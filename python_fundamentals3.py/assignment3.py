#Problem 1: palindrome
s=input("Enter the string: ")
i=0
j=len(s)-1
palindrome=False
while s[i]==s[j]:
    i+=1
    j-=1
    if i==j:
        palindrome=True
        break
       
print(f"This is palindrome: {palindrome}") 

#-----------------------------------------------------------------
#Probelm2: average on number in list
# L={1,2,9}

# sum=0
# for num in L:
#     sum+=num
# average= sum/len(L)
# print(f"Average of list is : {average}")

#-----------------------------------------------------------------
#Problem3: input 2 list from user rmerge them and sort
# l1=[]
# l2=[]
# print("Enter the list1:")
# for i in range(5):
#     s=int(input("Enter element: "))
#     l1.append(s)
# for i in range(5):
#     p=int(input("Enter element: "))
#     l2.append(p)
#     l1.append(p)

# l1.sort()

# print("Mergeed and sorted List: ",l1)

#-----------------------------------------------------------------
#Problem4: Given a tuple of integers, create:
# • 
# A tuple of all even numbers
# • 
# A tuple of all odd number

# tup=(2,6,8,3,4,9,8,7)

# odd=[]
# even=[]
# for num in tup:
#     if num%2 !=0:
#         odd.append(num)
#     else:
#         even.append(num)

# odd_tup=tuple(odd)
# even_tup=tuple(even)
# print("Even tuple:",even_tup)
# print(type(even_tup))
# print("Odd tuple: ",odd_tup)

#-----------------------------------------------------------------
#Problem5:Dictionary Problem
# students={
#     "Aditya":15,
#     "Varad":14,
#     "Shriram":14
# }
# def add_student():
#     name=input("Enter Student Name: ")
#     marks=int(input("marks: "))
#     students[name]=marks
#     print("Student added")

# def update_marks():
#     name=input("Enter Student Name: ")
#     marks=int(input("Marks: "))
#     if name in students:
#         students[name]=marks
#         print("Marks Updated")
# def search():
#      name=input("Enter Student Name: ")
#      if name in students:
#          print("Student exists")
#      else:
#          print("Students not exists")
# def display():
#     if students:
#         for name,marks in students.items():
#             print(f"{name}->{marks}")
#     else:
#         print("No Record Found!!!")

# def menu():
#     while True:
#         print("\n A-add student")
#         print("\n B-Updatewmarks")
#         print("\n C-search student")
#         print("\n D-display all student")
#         print("\n E-exit")
        
#         choice=input("Enter Choice : ").upper()
#         if choice=='A':
#             add_student()
#         elif choice=='B':
#             update_marks()
#         elif choice=='C':
#             search()
#         elif choice=='D':
#             display()
#         elif choice=='E':
#             break
#         else:
#             print("Invalid Choice")
# menu()

#-----------------------------------------------------------------
#Problem 6:list to dictionary mapping
# words=["apple", "banana", "kiwi", "cherry", "mango"]
# mapping={}
# for name in words:
#     mapping[name]=len(name)
# print(mapping)
#-----------------------------------------------------------------
#Problem7:
# m=input("Enter the string with Spaces: ")

# count=0
# for ch in m:
#     if ch==' ':
#         count+=1
# print(f"No. of spaces in String: {count}")
#-----------------------------------------------------------------
#Problem8:
list1 = [1, 2, 3] 
list2 = [3, 4]
s3= set(list1).intersection(set(list2))
print(f"Elements: {s3}")
#-----------------------------------------------------------------
#Problem9:
# list1=[1,2,3,4,5,6,7,8,9,2,4,7,5,3,5,1,9,3,5,6]
# seen=set()
# duplicate=set()
# for n in list1:
#     if n in seen:
#         duplicate.add(n)
#     else:
#         seen.add(n)

# print(f"Duplaictes are: {duplicate}")
#Problem10:
# s=input("Enter the sriing: ")
# unique=set(s)
# print("Unique chars: ",unique)
# print("Count:",len(unique))