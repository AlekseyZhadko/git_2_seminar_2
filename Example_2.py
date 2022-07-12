# Написать программу для проверки истинности утверждения, для всех значений предикат

def isPredicat(x,y,z):
    x = bool(x)
    y = bool(y)
    z = bool(z)
    if ~(x + y + z) == ~x * ~y * ~z:
        return True
    else:
        return False

print(isPredicat(0,0,0))
print(isPredicat(0,0,1))
print(isPredicat(0,1,1))
print(isPredicat(0,1,0))
print(isPredicat(1,1,1))
print(isPredicat(1,1,0))
print(isPredicat(1,0,0))
print(isPredicat(1,0,1))

