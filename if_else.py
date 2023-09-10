# a=int(input("Enter Your age: "))
# print('Your age is:', a)

# if(a>=18):
#     print("You can vote")
# else:
#     print("you can't vote") 


# # Q.1 write a program to check number is even or odd?

# num=int(input("Enter the number:"))
# if num % 2 == 0:
#     print("The number is Even")
# else:
#     print("The number is odd ")


# # Q.2 Write a program to check year is leap year or not
# year=int(input("Enter the Year:"))

# if year % 400 == 0:
#     print("Yes, it is a leap year!")
# elif year % 100 == 0:
#     print("No, it is not an leap year!")
# elif year % 4 == 0:
#     print("Yes, it is a leap Year!")
# else:
#     print("No, it is not a leap year")
# # Q.3 Write a program to check if a charecter is a vowel or consonant.

# s=input('Enter the Character:')
# vowels ="aieouAEIOU"
# if s in vowels:
#     print("it is vowel charecter!")
# else:
#     print("It is a consonant!")

# # Write a program to check number is positive, negative or zero

# r=int(input("Enter the number:"))
# if r < 0:
#     print("The no. is negative")
# elif r > 0:
#     print("The no. is positive")
# else:
#     print("The no. is zero")

# # Write a program to find the maximum b/w two numbers
# n1=int(input("Enter the number1:"))
# n2=int(input("Enter the number2:"))

# if n1 > n2:
#     print(n1) 
# else:
#     print(n2)


# # Write a program to find the maximum b/w three numbers
# num1=int(input("Enter the number1:"))
# num2=int(input("Enter the number2:"))
# num3=int(input("Enter the number3:"))

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# elif num3 >= num1 and num3 >= num2:
#     print(num3)
# else:
#     print("sorry")


# # Write a program  to check character is alphabet or not
# a=input("Enter your choice:")

# alphabets ='abcdefghijklmnopqrstuvwxyzABCDEFIJKLMNOPQRSTUVWXYZ'

# if a in alphabets:
#     print("Yes your choice is an Alphabet thank you!") 
# else:
#     print("No it is not an alphabets")


# # Write a program  to check character is any alphabet and check whether it is vowel or constant
# a=input("Enter your choice:")

# alphabets ='abcdefghijklmnopqrstuavwxyzABCDEFIJKLMNOPQRSTUVWXYZ'
# vowel = "aeiouAEIOU"

# if a in alphabets:

#     print("Yes your choice is an Alphabet thank you!") 
# else:
#     print("It is not an alphabet>.....")
# if a in vowel:
#     print("and it is a case of Vowel...")
# else:
#     print("It is a consonant")

# # Write a program to check if a number is divisible by 5  and 11
# num= int(input("Enter the number:"))

# if num % 5 == 0:
#     print("Yes number is divisible by 5")
# else:
#     print("Number not divisible by 5 but..")
# if num % 11 == 0:
#     print("Yes number is divisible by 11")
# else:
#     print("no Number is not divisible by 11")
# Q. write a program that capable of greeting you with Good Mornining , afternoon & evening 
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

hour=int(time.strftime("%H"))

if hour>=6 and hour<12:
    print("Good Morning ji!")
elif hour >= 12 and hour < 18:
    print("Good afternoon ji!!")
else:
    print("Good evening betu!!")