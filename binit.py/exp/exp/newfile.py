def add(dict):
    name = int(intput("name"))
    age  =  int(intput("age"))
    d.append({"name":name,"age":age})
def deletion (d):
    name = input("name to delete")
    for i in dict:
        if i["name"]==name:

             dict.remove(i)
dict={}
n=int(input("enter how many pairs of name and age do you want to enter"))
for i in range(n):
    name = input("enter name=")
    age  = int(input("enter age="))
    dict.update({name:age})
    print(dict)

    def addnewpair(key,value):
        dictionary.update ({key : value})
    def deletepair(key):
        dictionary.pop(key)





