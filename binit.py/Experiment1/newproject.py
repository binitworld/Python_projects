# name="Binit"
# age=18
#
# is_adult = True
#
# print(name)
# print(age)
# a="Tony"
# b="Stark"
# c=a + b;
# int(input("Age of tony is:"))
# print('Name:' , c)
# name= "Tony"
# last_name ="Stark"
# age=51
# print(name+" "+last_name)
# print('Age of tony :',age)
# is_geniune =True
# name=input("what is your name?")
# print("Hello Mr."+" "+name)
# name=input("Tony what is your super hero name?")
# print("Tony:My super Hero name is"+"  "+name)
# old_age = input('enter your old age:')
# new_age = int(old_age) + 4
# print( new_age)

# Find the sum of two number by taking input from user...
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=a+b;
# print("the sum of two numbers is:"+" "+str(c))

# """use oF string"""
# use of upper and lower case as string in python
# name= "Sunil Kappor"
# print(name.upper())
# print(name.lower())
# print(name)

#use of find operator of string
# name="Rajwan Swami"
# print(name.find('i'))

# use of replace string to insert new things
# name="IronMan"
# print(name.replace('Iron','Tony '))
# print(name)

# use of in operator to chake whether the string type is present or not
# name="Raja Ki Rani"
# print('Ki' in name)

# '''Useas df Arithmatic operators(+,-,*,/,%)'''

# Use of + operator
# print(5+4)

# use of - operator
# print(5-8)

# use of * operator
# print(2*4)

# use of / operator there is condition in division that when if u don't want the no.behind the decimal place we generally uses "//"
# print(5/2)
# print(12//2)

# use of remainder  operator(%)
# print(99%2)
# print(69%3)

# Use power operator(**)...
# print(5**3)
# print(2**5)

# use of shortcuts to calculate thing python
# i=5
# i+=2
# print(i)
# i-=2
# print(i)
# i*=2
# print(i)
#
# i/=2
# print(i)
#
# i**=2
# print(i)
# i%=2
# print(i)

# Operator Precedence in python
# a=2+5-(10*6)
# print(a)

# use of comments:to define your program which is helpful

# Comparison operators it returns otput of bollean value..
#use of > ,< >=,<=,==,!=
# print(3>2)
# print(5<2)
# print(3>=2)
# print(5<=2)
# print(1==1)
# print(2==6)
# print(2!=6)
# print(1!=1)

# use of if else statement

# str1 = input("Enter a string: ")
# str2 = input("Enter another string: ")
# print("Resultant string is: ",str1+str2)
#
#




# record()
# dic=dict()
# x=int(input("Enter number of records: "))
# def rec():
#     name=str(input("\nEnter name: "))
#     age=int(input("Enter age: "))
#     dic[name]=age
#
# def del_rec():
#     print("")
#     print(dic)
#     d=str(input("\nEnter name of person whose record is to be deleted:"))
#     del dic[d]
#     print("")
#     print(dic)
#
# def rec_upd():
#     print("")
#     print(dic)
#     d=str(input("\nEnter name of person whose record is to be updated: "))
#     update={}
#     u=int(input("Enter new age: "))
#     update={d:u}
#     dic.update(update)
#     print("")
#     print(dic)
#
# def rec_count():
#     c=0
#     for i in dic:
#         c+=1
#     return c
#
#
# ##Input initial records
# while(x!=0):
#     rec()
#     x=x-1
#
# ##Menu Driven
# while(True):
#     print("\n1.Add a record\n2.Delete a record\n3.Display dictionary\n4.Update\n5.Count Total records\n6.Exit\n")
#     a=int(input("\nEnter your choice: "))
#     if (a==1):
#         rec()
#
#     elif (a==2):
#         del_rec()
#
#     elif (a==3):
#         print("")
#         print(dic)
#
#     elif (a==4):
#         rec_upd()
#
#     elif (a==5):
#         print("Total records currently in dictionary are: ", rec_count())
#     else:
#         break

# Using try-except-else
# try:
#  print("Hello")
# except:
#  print("Something went wrong")
# else:
#  print("Nothing went wrong")
#
# #Using try-except-finally
# try:
#  print(x)
# except:
#  print("\nSomething went wrong")
# finally:
#  print("The 'try except' is finished")
#
# print("\n")
# #Using module
# import math
# y=math.sqrt(64)
# print(y)
# import random
# print(random.randrange(1,10))
#
# print("\n")
# #Raising exception
# x = -1
# if x < 0:
#  raise Exception("Sorry, no numbers below zero")


# Score = (20, 50, 70, 100)
# tup1 = (120, 150, 170)
#
# print(Score)
# print(tup1,"\n")
# print(Score[0])
# print(tup1[0],"\n")
# print(type(Score))
# print(type(tup1),"\n")
# print(len(Score))
# print(Score+tup1)
# print(2*Score)
# print(20 in Score,"\n")
# print(Score.count(20))
# print(Score.index(70))
#
# MyTuple = ('Binit' , 17 , 20 , 3000)
# Tuple2 = (100, 40)
# Tuple3 = ('King',)
#
# print("Prints Tuple using direct method:",MyTuple)
#
# print("\nPrints Tuple using for loop:")
# x = len(MyTuple)
# for i in range(0,x):
#     print(MyTuple[i],end=' ')
#
# print("\n\nUsing Slice:",MyTuple[1:])
# print("Using Slice:",MyTuple[:3])
#
# print("\nAdding Tuples:",MyTuple+Tuple2+Tuple3)
#
# print("\nMyTuple type:",type(MyTuple))




# dic=dict()
# n=int(input("Enter number of students: "))
# for i in range(n):
#     x=str(input("\nEnter name: "))
#     y=int(input("Enter age: "))
#     dic[x]=y
#
# print("\n",dic)
# print("\nSorted by name: ", sorted(dic.items(),key=lambda t:t[0]))
# print("Sorted by age: ", sorted(dic.items(),key=lambda t:t[1]))



#loops in pythons
# 1st=[10,20,30,40,50]
# product =

# num1=int(input("Enter the first num1:"))
# num2=int(input("Enter the seccond num2:"))
# # x=nu1+num2;
# print("the sum of two numbers:"+ "num1+num2")
# # try:
# #     print("sum of two number:")


# a=[1,3,4]
# try:
#     print("second element =%d" %(a[1]))
#
#     print("fourth element=%d"%(a[3]))
#
# except:
#     print("An error occured")
# d1=()
# print(type(d1))


# d1={}
#
# d2={"Binit":"burgger","Rohan":"Pani puri"}
# d2["ankit"] = "mitti"
# # del d2["ankit"]
# print(d2.keys())
#
# set1={1,2,3,4,5}
# print(set1)
# print(type(set1))


#PANDA in pyth0n
# from panda import*
# s=
# print()

  from tkinter import messagebox

  messagebox.showinfo("Information", "Informative message")

  messagebox.showerror("Error", "Error message")

  messagebox.showwarning("Warning", "Warning message")