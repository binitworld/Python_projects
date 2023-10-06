# Here name is a type of string that stores the vale either in '' or in a "" 
name = input('Enter your name:')

print("Hello!"+ name)

#1. To print this line how you can print it i.e, He said,"I want to eat an apple".
a="He said, \"I want to eat an apple"
print(a )
# Here in this situation we can insert \(backslash) to print the statement as it is in above question for string
# in another situation if we do not wnat to print the above question we also go for single qoute ('')like
b='He said, "I want to eat an apple'
print(b)   
#                       Multilines String 
#  in multiplelines string we have to use triple single or double qoutes'''/"""
c="""My life My Rule
I am the king , Ram is the Ram which is the real Truth , I admitted my mistakes 
today is 07th of september in 2023  still I'm working 
thank you soo much"""

print(c)
# Accessing the characters in string
nam="Bunny"
print(nam[0])
print(nam[1])
print(nam[2])

# As this is too much hectic for us to print these all strings so 
# "Looping through string"
print("lets use loop in this\n")
for character in nam:
    print(character)
