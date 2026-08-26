# CSV AND JSON
import pandas as pd
# df_csv = pd.read_csv("data.csv")  
# # importing data from csv file  
# df_json = pd.read_json("data.json")  # importing data from json file
l = [["Adam", 96], ["Eve", 75], ["Bob", 82], ["Charlie", 92]]  
df = pd.DataFrame(l, columns=["Name", "Marks"])
df.to_csv("output.csv")   
# exporting to csv  
df.to_csv("output.csv", index=False)  # exporting without index 
# df.to_json("output.json")   
# exporting to json