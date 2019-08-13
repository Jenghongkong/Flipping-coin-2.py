import random

x = 1
while x > 0:
    b = float(input("What kind of bias do your coins have?: "))
    for number in str(x):
        if random.random()*1 >b:
            print("coins flip %s has a value of head: True"%number)
            
        else:
            print("coins flip %s has a value of head: False"%number)
    x = x + 1



