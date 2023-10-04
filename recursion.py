# Write a recursive function to calculate the factorial of a number.



def factorial(n):
    if(n==0 or n==1 ):
        return 1
    else:
        return n * factorial(n-1)
n= int(input("Enter the number :"))

print ("Number :" , n)
print("Factorial :",factorial(n) )

# Write a recursive function to reverse a string.
def rev_string(string):
    if len(string)==0:
        return string
    else:
        return rev_string(string[1:])+ string[0]
    
input =input("Enter your string value : ")

reversed_string = rev_string(input)
print("The Reversed string :",reversed_string)
    
    