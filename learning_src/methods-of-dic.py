# There  are  the different methods of dictionary :
# 1. update()
# There  are  the different methods of dictionary :
# 1. update()
my_dict={}

a= input("Enter the key-value pairs separated by commas: ")
a=a.split(",")


if len(a)% 2 == 0:
    for i in range (0, len(a) ,2):
        key=a[i]
        value=a[i+1]
        my_dict[key] = value
    print("Your items in the dictionary are :" )
    print(my_dict)
else:
    print("Please enter the correct input ")