# accessing base class

# 1. Code Duplication

class BaseChai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

class Ginger(BaseChai):
    def __init__(self, type_, strength, milk):
        self.type = type_
        self.strength = strength
        self.milk = milk

# 2. Explicit method

class Garlic(BaseChai):
    def __init__(self, type_, strength, milk):
        BaseChai.__init__(self, type_, strength)
        self.milk = milk


# 3. Using Super
class Lemon(BaseChai):
    def __init__(self, type_, strength, milk):
        super.__init__(type_, strength)
        self.milk = milk