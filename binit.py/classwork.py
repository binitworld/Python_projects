# 3.1 python program to display the sum of two number

name=input("Enter your name: ")

print("Welcome ",name, "Now play with Python")

a=int(input("Enter the first number: "))

b=int(input("Enter the second number: "))

print("value of a and b are", a, b, sep=":")

d, e=[float(x) for x in input("Enter two numbers:").split(' ')]


print("sum of %d and %d is %d"%(a, b, a+b))

print("product of", d," and ",e," is: ",d*e);

print("result on dividing {0} by {1} is {2}".format(d,e,d/e))


print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(I,F,S))   

4:48 PM
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %.10f\nHi I am string ... My value is %s"%(I,F,S)) 