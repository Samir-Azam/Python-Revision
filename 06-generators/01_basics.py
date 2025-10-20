def gen():
    yield "My"
    yield "Name"
    yield "is"
    yield "Samir"
    yield "Azam"

store_reference = gen()

print(next(store_reference))
print(next(store_reference))
print(next(store_reference))
print(next(store_reference))
print(next(store_reference))