temp = input("max 4-digit binary number: ")
binary = ""
decimal = 0
if not (len(temp) == 4):
    for i in range(4 - len(temp)):
        binary += "0"
    binary += temp
else:
    binary = temp
for i in range(4):
    decimal += int(binary[len(binary)-i-1]) * (2 ** i)
print("Deciaml: " + str(decimal))