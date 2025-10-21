# creating a class 

class Movies:
    rating = 7.8
    watchOn = "Netflix"

# creating an object 

object_name = Movies()
# print(type(object_name))
# print(type(Movies))
# print(type(object_name) is Movies)

# accessing class properties 
print(Movies.rating)

print(object_name.rating)

object_name.watchOn = "JioHotstar"
del object_name.watchOn
print(Movies.watchOn)
print(object_name.watchOn)