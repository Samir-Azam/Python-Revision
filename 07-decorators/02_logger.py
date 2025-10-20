from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(user):   
        if (user.lower()=="admin"):
            return func(user)
        else : 
            print("You are not authorized to access this section")
            return None
    return wrapper

@logger
def func(user):
    print(f"Welcome {user} you are allowed to make changes")

func("admin")
func("user")