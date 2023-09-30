# Basic
s=[2,3,4,6,]
print(type(s))
print(s)


def list():
    l=[1,2,3,4,'Yes','bhojpuri', 'Bihar', 'Rajasthan','Dehradhun']
    print('The list example for',l)
    print(type(l))
    print(l[0])
    print(l[1])
    print(l[2])
    print(l[3])
    print(l[4])
    print(l[5])
    print(l[6])     
    print(l[7])
    print(l[8])
    print(l[-3])       #Negative indexing
    print(l[len(l)-3]) #Positive indexing
    print(l[8-2])      #Positive indexing
    print(l[6])        #Positive indexing
    if 3 in l:
        print("Yes there is ")
    elif 8 in l:
        print('Please update the list with your value..')
    else:
        print('No')
    print(l[:])
    print(l)

list()

# List Comprehension

lst = [i for i in range (8)]
print(lst)

