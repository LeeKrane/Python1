year = input("Jahr: ")
try:
    year = int(year)
except ValueError:
    print("Fehler")
    exit()
if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    leap_year = "Schaltjahr"
else:
    leap_year = "kein Schaltjahr"
print("{:d} | {:s}".format(year, leap_year))
