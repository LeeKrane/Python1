def exit_program():
    print("Fehler")
    exit()


a = input("ax: ")
b = input("b: ")
c = input("c: ")
try:
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    exit_program()
if a < 1:
    exit_program()
solution = (c - b) / a
if b < 0:
    operation = "-"
    b *= -1
else:
    operation = "+"
print("Die Gleichung {:.2f} {:s} {:.2f} = {:.2f} hat die Lösung x = {:.3f}".format(a, operation, b, c, solution))
