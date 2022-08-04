from math import *

x=0
y=0

def init(a,b=0):
    global x

    global y
    x = a
    y = b

def complex_sqrt(): 
    res='i'+str(sqrt(abs(x)))
    return res