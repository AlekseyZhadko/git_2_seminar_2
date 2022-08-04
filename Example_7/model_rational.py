from math import *

x=0
y=0

def init(a,b=0):
    global x

    global y
    x = a
    y = b

def rational_sum(): return x + y
def rational_div(): return x / y
def rational_mult(): return x * y
def rational_sub(): return x - y
def rational_pow_n(): return x**y

def rational_sqrt(): sqrt(x)
def rational_pow_2(): return x**2
def rational_fact(): return factorial(x)
def rational_sin(): return sin(x)
def rational_cos(): return cos(x)
def rational_tan(): return tan(x)


