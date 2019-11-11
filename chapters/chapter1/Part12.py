number = float(input("Dreistellige Zahl: "))
for i in range(2, 6):
    print("{:7d} * {:1d}". format(int(number), i))
    number *= i
for i in range(5, 1, -1):
    print("{:7d} / {:1d}". format(int(number), i))
    number /= i
print("{:7d}". format(int(number)))
