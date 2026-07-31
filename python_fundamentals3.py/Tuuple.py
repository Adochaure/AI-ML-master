#Tuple in python is collection of items
# ordered -> immutable -> Items cannot be changed after the tuple is created. 
#allow duplicates -> hetrogenous

#because tuple are imutable they are fatser than List

#indexing -> Slicing (same as list)
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
empty_tuple = ()  #empty tuple
print(t[0])  # 1
print(t[2:5])  # (3, 4, 5)
print(t[-1]) #9

#lopps same as tuple
for tis in t:
    print(tis)

#TUple methods 
#1. index(val)
print(t.index(2)) #1
print(t.index(5)) #4

#2.count(val)
t2= (1,2,3,3,3,3,6)
print(t2.count(3)) #4

