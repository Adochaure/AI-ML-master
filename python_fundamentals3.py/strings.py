str1 = "Hello World"
#string -> immutable

#len() -> to print length of string
print(len(str1))   # 11

#Concatenation
word1 = "Aditya"
word2 = "Chaure"

word = word1 + " " + word2
print(word)        # Aditya Chaure


#Loops on strings

s = "Python"
for ch in s:
    print(ch) # P y t h o n



#Zero based indexing 
print(s[0])  #p
print(s[3])  #n

#Slicing the string
#syntax -> string[start : stop : step]

#start -> index where slice starts
# stop -> index where slice ends
# step -> how many indices to move each forwrd time


print(s[0:3]) #Pyt
print(s[2:])  #thon
print(s[0:5:2]) #pto
print(s[::2]) #pto
print(s[::-1]) # nohtyp



#String formating

#using format() function

name = "Raju"
rs = 150
text = "YE {} ,{} rupya de re baba".format(name,rs)
print(text)

#using f-string

text = f"YE {name} ,{rs} rupya de re baba"
print(text)