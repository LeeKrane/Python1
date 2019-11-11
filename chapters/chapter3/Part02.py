start = input("Beginn: ")
end = input("Ende: ")

try:
    start = int(start)
    end = int(end)
except ValueError:
    print("Error")
    exit()

print("-------")
if end > start:
    for i in range(start, end):
        print(str(i) + " ", end='')
else:
    for i in range(start, end, -1):
        print(str(i) + " ", end='')
