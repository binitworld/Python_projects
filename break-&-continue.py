# _________________# Break Statement__________________________________

# for i in range(12):
#     if(i == 10):
#         break
#     print("7 x",i+1,"=",7*(i+1))


# ______________________# Continue statement___________________________

# for i in range(12):
#     if(i == 10):
#         continue
#     print("7 x",i+1,"=",7*(i+1))


# Write a program to print the numbers from 1 to 100, but skip the numbers that are multiples of 3.
# for j in range(1,101):
#     if j % 3 == 0:
#         break
#     print(j)

for i in range(1, 101):
    if i % 2 == 0:
        if i % 5 == 0:
            continue
        print(i)
