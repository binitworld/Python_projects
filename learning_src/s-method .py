# Methods of sets 
# 1.union 
city1 ={"Kota",'Sitamarhi','Delhi','Dehradhun','Chennai','Gujarat','kolkata','patna',}
city2 ={'Banglore','Gulf','kabul','oty''goa'}

r = city1.union(city2)
print(r)


# 2.intersection of set
visited_city1 ={"Kota",'Sitamarhi','Delhi','Dehradhun','Chennai','Gujarat','kolkata','patna',}
Not_visited_city2 ={'Banglore','Gulf','kabul','oty''goa',"Kota",'Sitamarhi','Delhi','Dehradhun'}

r = visited_city1.intersection(Not_visited_city2)

print(r)

# 2.symmetric difference
