from random import randrange

random_number = randrange(0, 100)
print(random_number)  # debug
number = input("Versuch 1: ")

for i in range(2, 8):
    try:
        num = int(number)
    except ValueError:
        print("\"{:s}\" ist ungültig!".format(number))
    if num < random_number:
        print("zu klein")
    elif num > random_number:
        print("zu groß")
    else:
        print("richtig")
        break
    if not i == 7:
        number = input("Versuch {:d}: ".format(i))
    else:
        print("verkackt")
