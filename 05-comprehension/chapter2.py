# set comprehension

favourite_chai = [
    "Masala Chai",
    "Lemon Tea",
    "Ginger Tea",
    "Ginger Tea",
    "Milk Tea",
    "Milk Tea",
    "Green Tea",
    "Green Tea"
]

unique_tea = {tea for tea in favourite_chai}
# This is same as set(favourite_chai)

print(unique_tea)


recipes = {
    "Masala Chai" : ["ginger", "cardamom", "clove"],
    "Elaichi Chai" : ["elaichi", "cardamom", "milk"],
    "Spicy Chai" : ["ginger", "black pepper", "clove"],
}

# This is one way of doing things
ingre = set()

for ingredients in recipes.values():
    for item in ingredients:
        ingre.add(item)

# print(ingre)

unique_spices = {item for ingre in recipes.values() for item in ingre}

print(unique_spices)