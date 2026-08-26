import pandas as pd
# Merging & Joining 
df_customers = pd.DataFrame({  
"customer_id": [1, 2, 3, 4], 
"name": ["Adam", "Bob", "Charlie", "Dave"]  
})  
df_orders = pd.DataFrame({  
"order_id": [101, 102, 103, 104], 
"customer_id": [2, 1, 4, 5], 
"amount": [250, 120, 300, 180]  
}) 
print(pd.merge(df_customers, df_orders, on="customer_id")    )
# Inner Join 
print(pd.merge(df_customers, df_orders, on="customer_id", how="left") )  # Left Join 
print(pd.merge(df_customers, df_orders, on="customer_id", how="right") ) # Right Join 
print(pd.merge(df_customers, df_orders, on="customer_id", how="outer")  )# Outer Join

import matplotlib.pyplot as plt
#Basic plot
df_orders["amount"].hist()
df3 =df_orders.plot(kind='scatter', x='amount', y='order_id')
plt.show()