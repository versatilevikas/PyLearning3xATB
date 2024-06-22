def say_hello_arg_dafault(name='Vikas'):
    print("Hello",name)

#*args--> any number of arguyments

def sum_three(a=1,b=1,c=1):
    return a+b+c

result=sum_three(2)
print(result)

def print_arguments(*args):
    for i in args:
        print(i, end= "--- ")
#print_arguments("pramad","vikas")

def make_pizza(*toppings,base):
    print(toppings,base)

#make_pizza("mushrooms",base="thin crust")
n=5
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
