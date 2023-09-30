# Write a Python program to check if a given string is a palindrome.
def is_palindrome(input_string):
    #Remove space and convert to lower case
    cleaned_string =input_string.replace("","").lower()


    #compare with its revrse
    return cleaned_string==cleaned_string[::-1]

user_input = input('Enter a string: ')

if is_palindrome(user_input):
    print("{user_iput} is a palindrome. ")
else:
    print("{user_input} is not a palindrome. ")