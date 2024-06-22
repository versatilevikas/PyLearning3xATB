import time
my_dict={'b':2,'w':1,'c':67}

# for i in range(100):
#     print(my_dict)

# decorators practice

def caltime(func):
    def wrapper():
        print(" hey this where things getting started")
        start= time.time()
        func()
        end= time.time()
        print(end-start)
    return wrapper
@caltime
def timeCheck():
    pass


timeCheck()