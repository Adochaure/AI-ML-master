#Grouping and aggregation

# df2.groupby("country")["income"].mean()  # mean income for each country 
# • Aggregations 
 
# df.sum() 
# df.mean() 
# df.count() 
# df.max() 
# df.min() 
# df.std() 

import pandas as pd
df = pd.DataFrame({
    "country":["india","america","China","Japan"],
    "income":[12000000,3000000,3000440,903444]
})
# for multiple aggregation use df.aggr()
df2 = df.groupby("country")["income"].agg(["mean", "min", "max"]) 
print(df2)
# rename aggregate  
df.groupby("country")["income"].agg(avg_salary="mean", max_salary="max")  
df.groupby("country").agg({   
"income": "mean"  
}) # aggregate on multiple cols  
df.groupby("country").agg(  
 
avg_salary= ("income", "mean")  
) # rename aggregates on multiple cols 


df = pd.DataFrame({  
"country": ["USA", "USA", "India", "India"],  
"year": [2020, 2021, 2020, 2021],  
"sales": [100, 120, 90, 110],  
"profit": [20, 25, 18, 22]  
})  
melted = df.melt(  
id_vars=["country", "year"],  
value_name="value"     
)  
# columns to keep  
value_vars=["sales", "profit"],  # columns to unpivot  
var_name="metric",    
# new column name for variable  
# new column name for value (default is value)  
print(melted)