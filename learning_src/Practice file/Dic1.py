# Accessing The Dictionary items

info = {'name':'Miraj', 'age' : '23', 'Eligible to Drink' : True}
for info, doc in info.items():
    print(f"{info}:{doc}")



# Write a function that takes a dictionary as input and returns a list of all the keys in the dictionary.
# a = input(" Enter the value of dictionaries :")

# a={
#     "":""
# }

# print (a)
a = {
    "":""
}

keys = get_keys(a)

print(keys)
