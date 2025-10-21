# mro- method resolution order

class A:
    label = "class A"
class B(A):
    label = "class B"
class C(A):
    label = "class C"
class D(C, B):
    pass

object = D()

print(object.label)
print(D.__mro__)