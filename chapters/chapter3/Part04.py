number = input("Zahl: ")

try:
    number = int(number)
except ValueError:
    print("Error")
    exit()

divisors = []
for i in range(number-1, 0, -1):
    if number % i == 0:
        divisors.append(i)
divisors.reverse()
print(divisors)
