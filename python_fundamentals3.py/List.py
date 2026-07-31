# a list is the collection of items in python
# ordered -> mutable -> can contain duplicates
# synatx []
# Heterogeneous – Can contain different data types. 
my_list  = [1,3,4,5,6,]
print(my_list)  
print(type(my_list))      # <class 'list'> 

my_list2 = [10, "Hello", 3.14, True, 10]    # hetrogenous list
print(type(my_list2))
print(my_list2) 


#list indexing

my_list = ["apple", "banana", "cherry"]  
print(my_list[0])  # apple  
print(my_list[1])  # banana  
print(my_list[-1]) # cherry (last element) 

#modify list
my_list2[1] = "Santra"
print(my_list2) 
# [10, 'Santra', 3.14, True, 10]


#Slicing - Slicing in lists is same as slicing in strings.  
# syntax -> list[start : end : step]
# End-> exclusive

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
# Simple Slice  
print(numbers[2:5])  # Output: [2, 3, 4]  
print(numbers[:4])   # Output: [0, 1, 2, 3] (from start to index 3) 
print(numbers[5:])   # Output: [5, 6, 7, 8, 9] (from index 5 to end) 
print(numbers[:])    # Output: [0,1,2,3,4,5,6,7,8,9] (copy of the whole list) 
# using STEP  
print(numbers[::2])  # Output: [0, 2, 4, 6, 8] (every2nd element) 
print(numbers[1::3])  # Output: [1, 4, 7] (start at 1, every 3rd element)  
# NEGATIVE slice  
print(numbers[-5:-2]) # Output: [5, 6, 7] (negative indexing from end) 

#List methods
nums = [4,7,2,1]
#1.len()
print(len(nums))    # 4
#2.append()
nums.append(7)
print(nums) #[4, 7, 2, 1, 7]
#3.insert
nums.insert(1,0)
print(nums) #[4, 0, 7, 2, 1, 7] at posion 1 -> 0 get inserted
#4.reverse()
nums.reverse()
print(nums) #[7, 1, 2, 7, 0, 4]

#Loops on Lists
numbers = [10, 20, 30, 40, 50]  
for num in numbers:  
    print(num) 

#Linear search 
target= 30
idx = 0
for num in numbers:
    if num == target:
        print(f"{target} found at index = {idx}")
    idx+=1
#30 found at index = 2

