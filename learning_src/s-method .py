a={7,8,9,10}
b={56,34,2,10}
print(a.union(b))
print(a.intersection(b))
print(type(a))

#to update the specific set we use thw update function 

Seta = input("Enter elements of the first set separated by commas: ")
Setb = input("Enter elements of the second set separated by commas: ")

# Split the input strings into lists and convert them to sets
set1 = set(map(int, Seta.split(',')))
set2 = set(map(int, Setb.split(',')))

# Update the first set with elements from the second set
set1.update(set2)

print("The updated value of set 1 is:", set1)

num1= input("Enter the First number  set separated by  ,: ")
num2= input("Enter the Second number  set separated by  ,: ")

test1=set(map(int,num1.split(',')))
test2=set(map(int,num2.split(',')))

# num1.intersection_update(num2)
test1.intersection_update(test2)

print("The updated Intersection value is :  ", test1)

# Symmetric_difference

w= input("Enter the Set first value of first number Separated by commas: ")
x= input("Enter the Set Second  value of Second number Separated by commas: ")

try1=set(map(int , w.split(',')))
try2=set(map(int , x.split(',')))

Symmetric_value=try1.symmetric_difference(try2)
print("The updated value or Symmetric Difference is : ", Symmetric_value)

# isdisjointset()

v= input("Enter the value of  the First number  separated by commas:")

f= input("Enter the value of  the Second number separated by commas :")

rest1=set(map(int, v.split(',')))
rest2=set(map(int, f.split(',')))

Return=rest1.isdisjoint(rest2)

print("The updated value after the disjoint set is : ", Return)


# issuperset()

city1=input("Enter the name of you are Knowing Cities of INDIA only : ")
city2=input("Enter the name of you are Knowing Excepts the  Cities of INDIA or may include few ones : ")

wake1= set(city1.split(','))
wake2= set(city2.split(','))

Tommy=wake1.issuperset(wake2)

print("The updated value is :", Tommy)