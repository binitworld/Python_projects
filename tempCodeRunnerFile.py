# 5 write a program to print the facti=orial of a number enter by an user
user=int(input("Enter the integer:"))
f=1
v=1
while v <= user:
    # print(v,end=",")
    f = f*v
    v = v+1
print("The factorial of your input is :",f)
# 5.1 practice set