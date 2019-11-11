def fakult(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    else:
        save = 1
        for i in range(2, n+1):
            save *= i
        return save


try:
    print(fakult(int(input("Fakultät von: "))))
except ValueError:
    print("Error")
