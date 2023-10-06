def calculateGmean(a,b):
    mean =(a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if (b>a):
        print("Second no.  is grater")
    else:
        print("first no. is grater or equal")

a =8
b= 9
isGreater(a,b)
calculateGmean(a,b)

c =5
d= 10

isGreater(c,d)
calculateGmean(c,d)

# _____________________________________________________________________________________________________
                                    #  Arguments
a =float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))


def average(a,b):
    print("The Average is:",(a+b)/2)


average(a,b)


def average(a,b):
    print("The Average is:",(a+b)/2)


average(a,b)


# 1.Write a function to calculate the factorial of a number.

def factotial(a):
    # factorial=1
    if a < 0:
        print("The factorial of negative number doesnot exist hmmm...")
    elif a == 0:
        return  1
    else:
        # for i in range(1,a+1):
        #     factorial = 1
        return a*factorial(a-1)
def factorial(n):
    """
    Calculates the factorial of a number.

    Args:
    n: The number whose factorial to calculate.

    Returns:
    The factorial of n.
    """
    if n < 0:
        raise ValueError("The factorial of a negative number is not defined.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# 3. Write a function to check wheter a no. is prime
num=int(input('Enter the integers:'))

def primenumber(num):
    if num <= 1:
        print('The number is not prime')
    else:
        for i in range (2,num):
            if num % i == 0:
                print ('The number is composite')
                break
            else:
                print("The Number is Prime")
primenumber(num)

# Q.4 Write a funtion to  convert decimal to binary.

ask=int(input('Enter The value  : '))

def binary_conversion(data):
    if data < 0:
        return "invalid input (negative number)"
    elif data == 0:
        return "0b0"
    else:
        binary =""
        while data > 0:
            remainder = data % 2
            binary = str(remainder) + binary
            data =data // 2
        return '0b' + binary
binary_result = binary_conversion(ask)
print(f"the binary representataion of {ask} is : {binary_result}")

