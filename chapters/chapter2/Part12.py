def exit_program():
    print("Error")
    exit()


def print_coordinates(coords):
    for coord in coords:
        print(coord)


x = input("X: ")
y = input("Y: ")
size = input("Size: ")
try:
    x = int(x)
    y = int(y)
    size = int(size)
    if x > size or y > size:
        exit_program()
    x = x + size + 1
    y = size - y + 1
except ValueError:
    exit_program()
coordinates = []
for i in range(1, size*2+2):
    coordinate = " "
    for j in range(1, size*2+2):
        if x == j and y == i:
            coordinate += "X "
        elif i == size+1:
            coordinate += "- "
        elif j == size+1:
            coordinate += "| "
        else:
            coordinate += ". "
    coordinates.append(coordinate)
print_coordinates(coordinates)
