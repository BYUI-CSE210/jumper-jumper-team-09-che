import random

def ganador():
    number = random.randint(1,9)
    return number

print("Vale", ganador() )
print("Renzo", ganador() )
print("Pablo", ganador())