number = input("Ganzzahl: ")
while True:
    try:
        n = int(number)
    except ValueError:
        print("\"{:s}\" ist ungültig!".format(number))
        number = input("Ganzzahl: ")
    else:
        print("Erfolg")
        break
