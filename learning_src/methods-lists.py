
# Method -1 Append method :in this method,  list.append() takes exactly one argument
l=[1,2,6,0]
print(l)
l.append(8,9)
print(l)

# Method -2 sort()
color=["Violet","Blue","Green","Yellow",'Orange',"Red"]
print(color)
color.sort()
print(color)
color.sort(reverse=True)
print(color)
D=[99,76,54,32,2,55,90,0,1,8,9,6,2]
print(D)
D.sort()
print(D)
D.sort(reverse=True)
print(D)

# Method -3   indexO()

c=["Violet","Indigo","Blue","Green","Yellow",'Orange',"Red"]

print(c.index("Green"))
print(c.index("Violet"))
print(c.index("Yellow"))
print(c.index("Yellow"))
print(c.index("Red"))
print(c.index("Blue"))
print(c.index("Indigo"))


# Method -4 count()

m=["Violet","Indigo","Blue","Green","Yellow",'Orange',"Red"]
print(m.count(m))
g=[99,76,54,32,2,55,90,0,1,8,9,6,2]
print(g.count(55))


# Method 5 copy()
deva=['Shivji','Vishnu','Ganesha','Ram']

devi=deva.copy()
print(devi)
# 

# Method - 6 insert()
devi=['Parvati','Laxmi','Sraswati','Sita']
devi.insert(2,123)
print(devi)

# method-7 extend()
guest=['Rest','Raja','Seema','Rajat','Nadia']
guest.extend("Mohit")
print(guest)


