#set is unorderd collection of unique elements
#unordered -> unique -> mutable ->can add or remove -> sett elemts must be immutable
my_set = {1,2,2,2,2,2,2,3,4,5}
print(my_set)  #{1,2,3,4,5}
print(type(my_set))  #<class 'set'>
print(len(my_set)) #5

emptyset = set()



# set methods

s = {10,20,30}

s.add(40)  #{10,20,30,40}
print(s)

s.remove(20) #{10,30,40}
print(s)

print(s.pop())

# Union & Intersection  
A = {1, 2, 3}  
B = {3, 4, 5}  

print( A.union(B))    # {1, 2, 3, 4, 5} 
print(A.intersection(B))  #{3}

print(A.intersection_update(B))
print(A)   #{3}  A-> changed inplace to {3}


#clear()

s.clear()  #-> exmpty the set

