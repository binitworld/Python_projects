dic ={
    "Mango" : "Food",
    "Pen" : "Stationary",
    "Water":"Liquid",
    "Lamp": "Object",
    56:"Coder"
}
print( dic[56]) 


#Create a dictionary that maps the names of fruits to their colors.

Fruits ={
    "apple" : "red", "Guava" : "Green" , "Kiwi" :"Brown", "Mango" : "Yellow" , "Barries" : "red"
} 

Mango_color = Fruits.get("Mango")
print(Mango_color)
print(Fruits)
for Fruits, color in Fruits.items():
    print(f"{Fruits}: {color}")

