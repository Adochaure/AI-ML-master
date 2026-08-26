#String cleaning
# .str.lower() -> convert to lowercase
# .str.upper() -> to uppercase
# .str.capitalize() -> capitalize string
# .str.strip() -> remover leaidng spaces
# .str.split(" ")-> split in to part on based on seperator
# .str.contains()->check if value exist in string

import pandas as pd

df  = pd.DataFrame({
    "name":["kp","ab","abc"]
    ,"age":[1,2,3],
    "income":[10000,20000,30000]
})

print(df["name"].str.upper())
print(df["name"].str.split(" "),type(df["name"].str.split(" ")[0]) )

print(df["name"].str.contains("abc"))
print(df["name"].str.contains("kp",case=True))


#Transforming data

#.apply()
df["age_plus_10"]= df['age'].apply(lambda x: x+10)
print(df)
df['name'] = df['name'].map({'kp':'KP', 'ab':'AB'})
df.assign(new_income = df["income"] * 1.1) 
print(df)

# replce()
df["name"]=df['name'].replace({
    "KP":"raju",
    "AB":"BABU",
    
})
print(df)


#renaming
df = pd.DataFrame({  
"A": [1, 2, 3],  
"B": [4, 5, 6],  
"C": [7, 8, 9] 
})  
# Rename columns A -> X, B -> Y  
df_renamed = df.rename(columns={"A": "X", "B": "Y"})  
print(df_renamed) 


# Sorting - values & index

df2  = pd.DataFrame({
    "name":["kp","ab","abc"]
    ,"Age":[1,2,3],
    "Income":[10000,20000,30000]
})

df2.sort_values("Income")    
# sort values in ascending 
df2.sort_values("Income", ascending=False) # sort values in descending 
df2.sort_values(["Age", "Income"]) # sorts age,if age same then sorts income  
sorted_df2 = df2.sort_values(["Age", "Income"])  
sorted_df2.sort_index()  
# Ranking  
df2["Ranking"] = df2["Income"].rank(ascending=False, method="dense") 
df2["Ranking"] = df2["Income"].rank(ascending=False, method="min") 
df2["Ranking"] = df2["Income"].rank(ascending=False, method="max") 