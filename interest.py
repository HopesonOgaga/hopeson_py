import math


def compound_interest():
    principal = float(input('enter principal: '))
    rate = float(input('enter the rate: ')) / 100
    n = float(input('enter the frequency: '))
    t = float(input('enter the overall tenure: '))
    c_i = principal * (1 + rate/n)**(n*t)
    return math.ceil(c_i)


print(f"your coumpound interest is ${compound_interest()}")