plz = input("Postleitzahl: ")
bezirk = int(plz[1]) * 10 + int(plz[2])
if 1 <= bezirk <= 23:
    print("Bezirk: {:02d}".format(bezirk))
