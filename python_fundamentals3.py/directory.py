# a directory is an unordered , mutable - key~value pairs

my_dict = {  
"name": "Shradha",  
"age": 30,  
"city": "Delhi" 
} 

# key -> unique
# key -> immutable
#Dictionary values can be anything (lists, other dictionaries, etc.) 


#accesing by [] and key
print(my_dict['age']) #30

#methods of directory
print(my_dict.keys())  #dict_keys(['name', 'age', 'city'])
print(my_dict.values()) #dict_values(['Shradha', 30, 'Delhi'])
print(my_dict.items())  #dict_items([('name', 'Shradha'), ('age', 30), ('city', 'Delhi')])


#get(key)  -> a safer way to access value of a particular key. Instead of throwing 
# an error it returns  if key doesn’t exist 

print(my_dict.get("cgpa"))   #None

new_item = {"cgpa":9.23}
my_dict.update(new_item)
print(my_dict) #{'name': 'Shradha', 'age': 30, 'city': 'Delhi', 'cgpa': 9.23}

#loops in directory
for key,value in my_dict.items():
    print(key,value)