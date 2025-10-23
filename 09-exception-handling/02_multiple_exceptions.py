# multiple exceptions


try:
    ingredients = ["cardamom", "lemon", "ginger"]
    print(ingredients[4])

    print(5/0)
except ZeroDivisionError as e:
    raise e("We can't divide any number by Zero...")

except IndexError as e:
    raise e("Index selected is out of bound...")
