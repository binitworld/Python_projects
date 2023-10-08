def set():
    employ={'raju','riti',44,True,8.9}
    return employ
employ=set()
print(employ)

# Create a set of unique characters from a string.

input_string =input("Enter the string to get the unique Char : ")

unique_character=set()

for r in input_string:
    unique_character.add(r)

print(unique_character)


# Find the union and intersection of two sets.

input_set1=input("Enter the number to find its union : ")
input_set2=input("Enter the number to find its union : ")

set1=set(input_set1.split(','))
set2=set(input_set2.split(','))

union_set = set1.union(set2)

intersection_set = set1.intersection(set2)

print("The union of two respective set is : ",union_set)
print("The intersection of two respective set is : ",intersection_set)

# sets are the un-order collection of data items which is separated by ','

