import math

a = input("Seite a: ")
b = input("Seite b: ")
c = input("Seite c: ")
s = (float(a) + float(b) + float(c))/2
print("Fläche: " + str(math.sqrt(s * (s - float(a)) * (s - float(b)) * (s - float(c)))))
