# Write a program  to check character is any alphabet and check whether it is vowel or constant
a=input("Enter your choice:")

alphabets ='abcdefghijklmnopqrstuvwxyzABCDEFIJKLMNOPQRSTUVWXYZ'
vowel = "aeiouAEIOU"

if a in alphabets:
    print("Yes your choice is an Alphabet thank you!") 
elif a in vowel:
    print("and it is a case of Vowel...")
else:
    print("It is a consonant")
