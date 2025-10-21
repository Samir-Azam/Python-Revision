# static methods

class Chai:

    @staticmethod
    def cleaned_ingredients(text):
        return [item.strip() for item in text.split(",")]

ingre = "milk   , cardamom, sugar, tealeaf, ginger"

# This is one way of doing things by creating object
# tea = Chai()
# cleaned = tea.cleaned_ingredients(ingre)


# other way of doing things using static methods
cleaned = Chai.cleaned_ingredients(ingre)
print(cleaned)