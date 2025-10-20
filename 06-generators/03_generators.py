# sending something to generators

def sending_generators():
    print("Welcome!!! to My Chai Lelo Bhai")
    order = yield
    while True:
        print(f"Preparing your order for {order}")
        order = yield

call_gen = sending_generators()
next(call_gen)
call_gen.send("Masala Tea")
call_gen.send("Coffe")
