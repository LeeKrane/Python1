import math

print("Programm zur Berechnung von Umfang, "
      "Fläche und Diagonale eines Quadrats")
a = input("Seitenlänge a = ")

# A = a * a Fehler : a ist ein String , wir wollen aber mit Zahlen rechnen
a = int( a )
A = a * a
A = a ** 2 # ** = > hoch
print ("Fl¨ache =", A )
d = math . sqrt (2 * a ** 2) # 2a^2
print (" Diagonale =", d )