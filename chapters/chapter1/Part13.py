number = int(input("Zahl: "))
print(str(number) + " = " + str(int(number / 100)) + " * 100 + " + str(int(number % 100 / 10)) + " * 10 + " + str(int(number % 10)) + " * 1")
