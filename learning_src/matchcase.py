x = int(input("Enter the number:"))

match x:
    case 0:
        print("x is zero")
    case 4:
        print('case is 4')
    case _:
        print(x) 


# ____________________________________________________________________________
# Write a program to check if a number is evwn or odd using match case

num=int(input("Enter a number:"))

match num % 2:
    case 0:
        print("The given number is Even")
    case _:
        print("The no is Odd")

# # ________________________________________________________________________________

# # Write a python program to check if a string is a palindrome using match case statement

# '''string =input("Enter a string:")
# # Remove spaces and convert to lower case for a case insensitive check
# cleaned_string= string.replace(" ","").lower()

# match cleaned_string == cleaned_string[::-1]:
#     case 0: 
#         print("This is a palliindrime type ")
#     case _:
#         print("Enter the correct string as it is not a palidrome")'''


# '''def is_palindrome(string):
#     match string:
#         case string[::-1]:
#             print("The entered string is a palindrome.")
#         case _:
#             print("It is not a palindrome.")

# input_string = input("Enter a string: ")
# is_palindrome(input_string)'''

# _______________________________________________________________________________________________________________________
#Write a python program to check if a year is a leap  year using  match case statement 
year= input("Enter the year:")
match year/400 == 0:
    case 0:
        print("yes it is a leap year!!")
    case _:
        print (" No it is not aleap year")


# Write a program to check if a character is a letter , adigit, or a special character using  matc case statement
input=input("Enter the value:")

# num="0123456789"
# alphabet="abcdefghijklmnopqrstuvwxyz"
match input:
    case m if m.isnumeric():
        print("It is a number")
    case m if m.isalpha():
        print("It is alphabet")
    case _:
        print("It is a special case")
