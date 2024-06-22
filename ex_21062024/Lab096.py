#decorators==essentially a fn which takes another fn as an argument and returns a new function

def my_decorator(func):
    def wrapper():
        print("starting")
        print("*************")
        func()
        print("**************")
        print("End")
    return wrapper()

@my_decorator
def say_hello():
    print("say Hello")
