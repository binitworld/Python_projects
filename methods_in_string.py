# Converting the given strings into upper case
nom="harshchu"
print(nom.upper())  #here we uses the .upper()to locate the given string in 'nom'to be in uppercase
# Converting the given string  in lowercase by taking the input frm user
Name=input('Enter your name in capital letter:')
print("My name is",Name.lower() , "Thank you ji for asking!!")

# .strip() === it is uses for removing the spaces b/w and in starting or end  any string.
d=" Dance,Music "
print('it removes all the spaces and your result is like', d.strip())
# .rstrip()
print("It can add the value",d.rstrip("!"))
# Use of replce ()method
print("see this",d.replace("Dance","Music"))
# # Now split()method in string speprated it in string
# print("Return this",d.split(''))
beta="introducton in python in python"
cap=beta.capitalize()
print('This will captalise the string and modify it see:\n',cap)
# cot=beta.count()
print('This will usually count the value:\n',beta.count(""))


