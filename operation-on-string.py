# Lets talks about String slicing 
names="King,Coder"
print(names[0:4])

# For finding lenth of the string we uses the len function 

print(len(names))

#so comma',' is also a string type 

# take an example

animals="Ceetah,zebra,cow,dog"
len1=len(animals)
print("For all animals",len1 , "letter words")
print(len1)
# see the example of  slicing in python /string 
print(animals[:6])
print(animals[:])

# 2. solve one question {Take an user input and use for loop and print that input i outpt of specific character}
Userinput=input("Enter your chooised Alphabets:\n ")

for i in Userinput:
    print(i)

# Quiz type for slicing
no="KIGHT"
print(no[-4:-2])