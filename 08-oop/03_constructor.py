# in python __init__ method is also used to initialize values into an object and it is also said as constructor

class Youtubers:

    # constructor
    def __init__ (self, name, subscribers):
        self.name = name
        self.subscribers = subscribers
    
    def show_data(self):
        print(f"{self.name} has {self.subscribers} million subscribers")


yt1 = Youtubers("Fukra Insaan", 13)
yt1.show_data()