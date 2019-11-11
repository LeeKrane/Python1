centigrade = input("Temperatur in Grad Celsius: ")
try:
    centigrade = float(centigrade)
except ValueError:
    print("Ungültige Eingabe!")
    exit()
fahrenheit = centigrade / 5 * 9 + 32
kelvin = centigrade + 273.15
if kelvin < 0:
    print("Eingabe zu niedring!")
    exit()
print("°C: {:.2f} | °F: {:.2f} | K: {:.2f}".format(centigrade, fahrenheit, kelvin))
