#1. Write a program to take the user's name as input and print it?
x = input("Your Name=")
print("My name is", x)

#2. Wrie a program to take user's age as input and print it?

age = input("Your age=")
print('And my age is', age)

#3. Write a program to take two numbers as input and print there sum

q = input("Enter the First number=")
r = input("Enter the Second number=")
print("Sum of two nois:",int(q)+int(r),)

# 4. write a program to take  of three numbers as input and print there average
a = float(input("Enter the value of   a ="))
b = float(input("Enter the value of   b= "))
c = float(input("Enter ther value of  c= "))

average = (a + b + c) / 3
print("The average of these three number  is:", average)

# 5. Write a program to take a string as input and print its length

m = input("Enter your fav string:: ")
string = len(m)
print("The lenth of your chosen string is:",string)

# 6. Write  a program take a character as input and print its ASCII code.
a=input("Enter your character:")
if len(a) == 1:
    ascii_code = ord(a)
    print("The ASCII code as per your input is:",ascii_code)
else:
    print("Please enter singe chr.")

# # 7. Write a program to take a list of numbers as input and print the lasrgest number among them
B = input("Enter the all your list of numbers:")

# spliting the imput numbers into indivisual numbers & converting them into the integers
numbers = [int(num) for num in B.replace(',','').split() if num]
# checking the list of the B 
if numbers:
    B =max(numbers)
    print("the largest number in your given List is:",B)
else:
    print("The list is empty. Please enter the required datain your list:",B)

# 8. Write a program to take alist of stringsas input and print the longest string 
input_string=input("Enter a list of strings seprated by space: ")

string = input_string.split()
if string:
    longest_string = max(string, key=len)
    print("The longest string inthe list is",longest_string)
else:
    print("The list is empty")
