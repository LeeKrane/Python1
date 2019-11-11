r = 5
for i in range(1, r+1):
    out = ""
    for j in range(i):
        out += "* "
    print(out)
for i in range(r-1, 0, -1):
    out = ""
    for j in range(i):
        out += "* "
    print(out)
