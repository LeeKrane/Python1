a = input("a: ")
b = input("b: ")
c = input("c: ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
except ValueError:
    print("Error")
    exit()

if a > b:
    h = a
    a = b
    b = h
if b > c:
    h = b
    b = c
    c = h
if a > b:
    h = a
    a = b
    b = h
print("{:d}, {:d}, {:d}".format(a, b, c))
