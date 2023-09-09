# Q. write a program that capable of greeting you with Good Mornining , afternoon & evening 
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

hour=int(time.strftime("%H"))

if hour>=6 and hour<12:
    print("Good Morning ji!")
elif hour >= 12 and hour < 18:
    print("Good afternoon ji!!")
else:
    print("Good evening betu!!")