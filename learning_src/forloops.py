# ____________________________For Loops___________________________________________________--
c=["Yellow , Black, Purple,White,Brown"]
for color in c:
    print(color,end=" ,")
    for i in color:
        print(i,end=",")

# Use of Range()
x=int(input("Enter the value:"))

for i in range(x):
    print(i+1,end=",")

# Q1. Write a program to print the number fro 1 to 10
for j in range(10):
    print(i+1)

# Q2. Write a program to print the even no. from 1 to 100
for x in range(101):
    if x % 2 ==0:
        print(x,end=",")


# Q3. Write a program to print the square of all number from 1 to 10
for sq in range(11):
    print(sq*sq)


# Write a Program to print the fibonacci Sequence upt 10th term

'''m=int (input('Enter the value:'))

for fib in range (m):
    if fib == 0:
        print(fib)
    else:
        print(fib(n-2)+fib(n-2))
'''

# Write a program to reverse a String

st=input('Enter the string:')
Reversed_string=''

for i in range(len(st)-1,-1,-1):
    Reversed_string += st[i]

print('The reversed string here is:',Reversed_string)

# practice-1
s=input("Enter the sring:")
r_string=''
for i in range(len(s)-1,-1,-1):
    r_string += s[i]
print('Your reversed form of string is:',r_string)

# Write a program to print the all prime no. in b/w 1 to 100
print('The prime no.s b/w 1 to 100 are:')

for num in range(2, 100):
    is_prime = True
    
    for i in range (2, int(num ** 0.5) +1) :

        if num % i == 0:
            is_prime = False
        if is_prime:
            print(num)

# teest casst
for i in range (1,6):
    print('{}{}'.format(str(i),str(i) *(i-1)))