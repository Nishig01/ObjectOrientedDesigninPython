#Decorators==> a fn that extends the behavior of another fn w/o modifying the base fn
#              Pass the base fn as an argument to the decorator

#             @add_sprinkels
#             get_ice_cream("vanilla")


# we need a wrapper so that decorator doesn't gets called as soon as its declared

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🪄*")
        func(*args, **kwargs)# basefn get_ice_cream accepts many arguments and keyword arguemnts
    return wrapper


def add_straw(func):
    print("*You add strwa 🪄*")
    func()

# @add_straw
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your ice cream 🍦{flavor}")

get_ice_cream("Vanilla")
get_ice_cream("Banana")
# *You add sprinkles 🪄*
# Here is your ice cream 🍦

