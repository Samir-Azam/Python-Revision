# infinite generators

def infinite_call():

    count = 1
    while True:
        yield f"Refill #{count}"
        count +=1

user1 = infinite_call()
user2 = infinite_call()

# refill count for user1 
for _ in range(5):
    print(next(user1))

# refill count for user2
for _ in range(10):
    print(next(user2))