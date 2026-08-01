#List Comprehension is a short and elegant way to create lists in Python.  
# It replaces long  for  loops with one-line expressions.

# syntax -> [expression for item in iterable]

nums = [x for x in range(1,6)]
print(nums)

#List Comprehension with Condition 
#syntax -> [expression for item in iterable if condition]

evens = [x for x in range(1,20) if x%2==0]
print(evens)

#List comprehension with if-else
# [expression_if_true if condition else expression_if_false for item in iterable] 

labels = ["Even" if x%2==0 else "Odd" for x in range(1,20)]
print(labels)


