# format string in the python


letter =" Hey my name is {} ans I am from {} "
country ="India"
name = "Binit"

# basic senario
print(letter.format(name, country))

# Un-basic senario

letter ="Hey!! my name is {0} and i am from {1} "
# letter ="Hey!! my name is {1} and I'm  from {0}"
name = "Binit"
country = " India "
print(letter.format(country,name))
print(letter.format(name,country))

# Letts talks about f-string
def fstring(name,country):
    print(f"Hey!! my name is {name} and I belongs from {country}")
name =input("Enter your name:")
country =input("Enter your country:")
fstring(name,country)

# For taking decimal upto two decimal place we can take use of .2f
def useof2f():
    price =float(input("Enter the amount in $ usd:"))
    txt= "for only {:.2f} $usd"
    print(txt.format(price))

useof2f()

