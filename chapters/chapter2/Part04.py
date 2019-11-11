from random import randrange

a = randrange(100, 401)
b = randrange(100, 401)

if a < b:
    print("{:3d} < {:3d}".format(a, b))
else:
    print("{:3d} < {:3d}".format(b, a))
