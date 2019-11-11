nettopreis = input("Netto: ")
steuer = input("Steuer: ")
print("Brutto: " + str(float(nettopreis) * (float(steuer) / 100 + 1)))
