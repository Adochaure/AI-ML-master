import pandas as pd
import numpy as np
data = {  
'Name': ['Aarav', 'Isha', 'Rohan', 'Sneha', 'Vikram'],  
'Age': [25, 30, 35, 40, 45],  
'City': ['Delhi', 'Mumbai','null', 'Kolkata', 'Chennai'],
'Salary':[30000,58000,56000,34000,12000]  
}  
df = pd.DataFrame(data)  
print(df.head())  
print(df.tail())  
print(df.sample())  
print(df.info())  
print(df.describe())  
print(df.nunique())  
print(df.dtypes)  
print(df.shape)  
print(df.columns) 


#Selecign rows
# by index label loc
df.loc[0]
df.loc[0:3]
df.loc[0,"City"]

#by index positon iloc
df.iloc[0]   # 1st row 
df.iloc[4:7]   # 1st row 
df.iloc[0, 2]  # 1st row & 3rd column (by position)
# iloc in slice ending index is not inclusive

# # selcting single cell use 
# df.at[0]
# df.iat[0,2]


#Boolean filtering
df[df['Age'] > 30]  
print(df[(df['Age'] > 30) & (df['Salary'] > 50000)] )

#for sql like filtering -> df.query()
print(df.query("Age > 30 and Salary >50000"))

my_city ="Bangalore"
print(df.query("City == @my_city"))

# Query returns a COPY, not a VIEW. 


#--------------------------------------------------

#Handling misssing values(NAN)

print(df.isnull())  # Shows boolean DataFrame, True where NaN
print(df.isnull().sum())  #count of NAN per col
df.dropna()  #drops rows with any NAN
df.fillna(4) #fills NAN with value

df.ffill() #Forward Fill (carry previous value) 
df.bfill() #abckward fill


#handle duplicates
df.duplicated()  #true for duplicate rows
df.duplicated("City")  #in particulat row
df.drop_duplicates() #drops duplicate rows

#chnaging datatypes
# df.astype(float128)




