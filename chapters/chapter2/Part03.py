plz = input("Postleitzahl: ")
bezirk = int(plz[1]) * 10 + int(plz[2])
if bezirk < 1 or bezirk > 23 or not int(plz[0]) == 1:
    print("Fehler")
    exit()
print("{:4d} | {:d}. Bezirk".format(int(plz), bezirk))
