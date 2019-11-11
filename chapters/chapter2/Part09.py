def exit_program():
    print("Fehler")
    exit()


def valid_month():
    if not 1 <= month <= 12:
        exit_program()


year = input("Jahr: ")
month = input("Monat: ")
try:
    year = int(year)
    month = int(month)
except ValueError:
    exit_program()
months_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days = months_days.get(month)
if month == 2 and (year % 4 == 0 and not year % 100 == 0 or year % 400 == 0):
    days += 1
print("Der Monat hat {:d} Tage.".format(days))
