n = input("Zahl: ")
try:
    n = int(n)
except ValueError:
    print("Fehler. Erwartet war eine Zahl; Eingabe: " + n)
    exit()
if n < 0:
    positive = "negativ"
else:
    positive = "positiv"
if n % 2 == 0:
    even = "gerade"
else:
    even = "ungerade"
print("Die Zahl ist {:s} und {:s}.".format(n, positive, even))
