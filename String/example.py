food = "pasta"
food.replace("a", "e")  # so here we know string are immutable so the change value arenot save in any variable so print food will print the value which is save in food variable
print(food)


food = "pasta"
food = food.replace("a", "e")
print(food)  # here it searches all letters and replace the matching one

# we can replace specific letter by assign there index value tooo

food = "pasta"
food = food.replace("a", "e", 1)
print(food)


list=["riya","pabitra"]
list.append("riyan")
print(list)