#python library for data analyis built on top of numpy -> make easier to work with
# hetrogenous , tabular labeled datasets

#Usage
#Pandas introduced to independant data structure called SERIES & DATAFRAME
import pandas as pd
df = pd.DataFrame({
    "name":["Aditya","sumit","Varad"],
    "Cgpa":[9,8,7]
})

print(df)


# ---------------------------------------------------------------------------------#

#SERIES -> 1d - labelded array hold any data type -> value , index
s = pd.Series([9,7,5,4,2,1])
print(s)
print(type(s))   #dtype: int64

#indexing
print(s[0])   #9
print(s[3])   #4
print(s.index)   #RangeIndex(start=0, stop=6, step=1)

#characteristics od SERIES
# 1.homogeneous- store one type of data
# 2.vectorization suppot
# 3.handle missing values with NAN
# 4.mutable value but immutable size


# custom indexing
s2 = pd.Series([1,2,3,4,5], index=['ado','sdo','kdo','rdo','cdo'])
print(s2["ado"])   #1
print(s2["sdo"])   #2

# vectorization
s3 = pd.Series([1,2,3,4,5])
s4 = pd.Series([9,8,7,6,5,6])
print(s3+s4)

#mutable value -> immutable size
s3[0] = 100
print(s3) #chnaged 1 -> 100
changed_s = s3.drop(1)
print(changed_s)
print(s3)


#---------------------------------------------------------

#Dataframe -> 2D , tabular data structure 
#USage
# Creating DataFrame in pandas - using dictionary  
info = {  
"Name" : ["Adam", "Eve", "Bob"],  
"Marks" : [78, 99, 85],  
"Grade" : ['B', 'O', 'A']  
}  
df = pd.DataFrame(info) 
print(df)

print(df.index)   # row labels 
print(df.columns) # column labels  

import numpy as np
# Creating DataFrom using Numpy array  
np_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
df = pd.DataFrame(np_arr, columns=["Col1", "Col2", "Col3"])  
print(df) 

# Creating DataFrom using Lists  
l = [["Adam", 96], ["Eve", 75], ["Bob", 82], ["Charlie", 92]]  
df = pd.DataFrame(l, columns=["Name", "Marks"])  
print(df)


