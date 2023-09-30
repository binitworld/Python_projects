# variable Tutorial -- By Binit 

a =1j
b= 'codetime'
c= 98
d= None

print (a )
print ( b)
print(c-a)
'''  
if a==complex:  In this line the code will give the output as the sorry  a is not complex
    print('Yes a is complex')
else:
    print('sorry a is not complex')

'''
if isinstance(a, complex):
    print('Yes a is complex')
else:
    print('sorry a is not complex')

print('the type of a is', type (a))
print('the type of b is', type (b))
print('the type of c is', type (c))
print('the type of d is', type (d))

# a collection of items is called as 'list'
list = [9,8,7,5  , ['moccow','Russia', 'India']  , ['banana','Apple','orranges']]

print(list)

# abundant key value pairs is also known as Dictionary / maap type of data 

dict = {'name:Ram', 'Ram age=20','wife=Sita', 'eligible to marry=true' ,'Sita age=22'}
print(dict)