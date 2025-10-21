class BaseChai:

    def __init__(self, type_):
        self.type = type_
    
    def preparing(self):
        print(f"Preparing {self.type} chai")

# inheritance
class Masala(BaseChai):

    def add_spices(self):
        print("Adding ginger, teaLeaf and elaichi")

class ChaiShop:

    # composition
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"{self.chai.type}")
        self.chai.preparing()


shop = ChaiShop()

shop.serve()
