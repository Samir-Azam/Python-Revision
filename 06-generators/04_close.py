# closing generators and yield from 


def chai():
    yield "Masala Tea"
    yield "Ice Tea"

def coffee():
    yield "Coffee"
    yield "Latte"

def menu():
    yield from chai()
    yield from coffee()

menu_list = menu()
for item in menu_list:
    print(item)
