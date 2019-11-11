def exit_program():
    print("Fehler")
    exit()


def print_money_values(money):
    money += 1
    bank_notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    for i in bank_notes:
        counter = 0
        while money - i > 0:
            counter += 1
            money -= i
        if counter > 0:
            print("{:d}x {:3d}".format(counter, i))


zu_zahlen = input("Zu zahlen: ")
erhalten = input("Erhalten: ")
try:
    zu_zahlen = int(zu_zahlen)
    erhalten = int(erhalten)
except ValueError:
    exit_program()
if zu_zahlen < 0 or erhalten < 0 or erhalten < zu_zahlen:
    exit_program()
print("Retour:")
print_money_values(erhalten - zu_zahlen)
