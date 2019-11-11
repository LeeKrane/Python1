inp = int(input("Sekunden: "))
h = 0
m = 0
s = 0

while inp > 0:
    s += 1
    if s >= 60:
        s = 0
        m += 1
    if m >= 60:
        m = 0
        h += 1
    inp -= 1

print("{:02d}:{:02d}:{:02d}". format(h, m, s))
