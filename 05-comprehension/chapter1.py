# list comprehension
menu = [
    "Masala Tea",
    "Iced Tea",
    "Lemon Tea",
    "Iced Lemon Tea",
    "Hot Tea"
]

# if we want to filter out only Iced Tea

iced = [tea for tea in menu if "Iced" in tea]
print(iced)