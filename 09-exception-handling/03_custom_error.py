# creating custom errors

class FemaleInteractionError(Exception):
    pass


raise FemaleInteractionError("No any Female Interaction since birth")