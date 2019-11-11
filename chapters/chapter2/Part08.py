def exit_program():
    print("Fehler")
    exit()


a = input("First Number: ")
b = input("Second Number: ")
try:
    a = float(a)
    b = float(b)
except ValueError:
    exit_program()
operation = input("Operation: ")
if operation == "+":
    c = a + b
elif operation == "-":
    c = a - b
elif operation == "*":
    c = a * b
elif operation == "/":
    if b == 0:
        exit_program()
    c = a / b
else:
    exit_program()
print("-------\n{:.3f} {:s} {:.3f} = {:.3f}".format(a, operation, b, c))
