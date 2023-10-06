i= int (input("Enter the integer:"))

current_num = 1

while current_num <= i:
    print(current_num)
    current_num =current_num+1

# 1. write a Program to print the numbers from 1 to 10 using while loop
z = 1 #As it strat with one
while z<=10: #this line shows that it will use the loop from 1 to 10
    print(z)
    z= z+1 

# 2.Write a program to print  the even numbers from 1 to 100

d=1
while d <= 100:
    if d % 2 == 0:
        print('The even no b/w 1 to 100:',d)
    d=d+1

# 3,Write a program to print the fibonacci series upto 20th term using a while loop

a1 , a2 = 0 , 1
c = 0
while c<=10 :
    print( a1 ,end=" ,")
    a1,a2=a2,a1+a2
    c += 1

#4. Write a program to print squares of  all number upto 10
m=1
while m<=10:
    # if m*m >=0:  it is unnecessary as all squares of real no. are +ve:
    print(m*m,end=",")
    m = m+1

# 4.1practice set (in this Taking the input from user that upto which integer they want to print )

user_input=int(input("Enter your integer:"))

x=1
while x<=user_input:
    print(x*x,end=",")
    x = x+1

# 5 write a program to print the facti=orial of a number enter by an user
user=int(input("Enter the integer:"))
f=1
v=1
while v <= user:
    # print(v,end=",")
    f = f*v
    v = v+1
print("The factorial of your input is :",f)
# # 5.1 practice set
input=int(input("Enter the integer:"))
p=1
factotorial=1
while p <= input:
    factotorial =factotorial*p
    p = p+1
print("The factorial is:",factotorial)

# 6. Write a program to reverse a string using while loop

R=input('Enter a string:')

m = R[::-1]
while m <= R:
    print (m)

# 7.Write a program to print all the prime numbers from 1 to 100 using a while loop.
j=1
while j <= 100 :
    print(j,end=",")
    j = j+1

# Write a program to find the first 1000 Fibonacci numbers using a while loop.

a1,a2 =0,1

l = 0

while l<=1000:
    print(a1,end=",")
    a1,a2=a2,a1+a2
    l += 1