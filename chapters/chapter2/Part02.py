zu_zahlen = float(input("Zu zahlen: "))
if zu_zahlen < 0:
    print("Fehler")
    exit()
erhalten = float(input("Erhalten: "))
if erhalten < 0 or erhalten < zu_zahlen:
    print("Fehler")
    exit()
print("Rückgeld: " + str(erhalten - zu_zahlen))
