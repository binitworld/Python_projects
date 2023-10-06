# If there we had written som type of function the doc string just help us to understand that function 


def square(n):
    '''take in a number n , returns the square of n''' 
    return n**2
n = int(input('Enter the Digit to print:'))
result = square(n)
print("The Square is ", result)

print(square.__doc__)

# 1. Write a docstring for a function that takes two numbers as input and returns their sum.
def sum(a,b):
    '''This is the function for addition of two numbers as per the user input.  
    Thanks!! '''
    return a + b
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
m = sum(a,b)
print(' The sum of a+b is   :',m) 

print(sum.__doc__)

# Write a docstring for a class that represents a circle. The class should have methods to calculate the circle's area, circumference, and diameter.

def circle(r):
    '''Here, It is the function of a circle that will take the user input about the radius of circle as per it will provides: The Circles  
    1.Diameter
    2.area
    and 3. the circumference  '''
    diameter=2*r,
    Area =3.141*r**2,
    circumference=2*3.141*r
    return {
        'Diameter':diameter,
        'Area': Area,
        'Circumference':circumference
    }
r=float(input(" Enter the radius of circle :"))
circle_properties = circle(r)
print(circle_properties)

print(circle.__doc__)


# Write a docstring for a module that contains functions for performing common mathematical operations, such as addition, subtraction, multiplication, and division.
def mathematical_operations(j,k):
    '''This is a mathematical Operation program through which we can do these operations '''
    sum = j+k,
    Subtraction = j-k,
    multiplication = j*k,
    division = j/k
    return{
        'Addition': sum,
        'Subtraction': Subtraction,
        'Multiplication' : multiplication,
        'Division': division
    }
j=int(input("Enter Your first number :"))
k=int(input("Enter Your Second number :"))

maths = mathematical_operations(j,k)
print(maths)

print(mathematical_operations.__doc__)


# Write a docstring for a module that contains functions for performing common mathematical operations, such as addition, subtraction, multiplication, and division.

def average(numbers):
    '''This function calculates the average of a list of numbers.'''
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

# Prompt the user for a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in user_input.split()]

# Call the average function and print the result
result = average(numbers)
print("Average:", result)

# Print the docstring
print(average.__doc__)









