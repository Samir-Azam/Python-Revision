# class method vs static method


class Tea:

    def __init__ (self, tea_type, cup_size, milk):
        self.tea_type = tea_type
        self.cup_size = cup_size
        self.milk = milk

    @classmethod
    def dict_format(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["cup_size"],
            order_data["milk"]
        )
    
    @classmethod
    def string_format(cls, order_data):
        tea_type, cup_size, milk = order_data.split("-")
        return cls(tea_type, cup_size, milk)
        

# object creation using class methods
order = Tea.dict_format({"tea_type":"masala", "cup_size":"Large", "milk":"hot"})

print(order.cup_size)
print(order.tea_type)
print(order.milk)

order = Tea.string_format("Lemon-medium-not needed")
print(order.cup_size)
print(order.tea_type)
print(order.milk)
