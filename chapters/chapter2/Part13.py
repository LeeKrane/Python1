def exit_program():
    print("Error")
    exit()


points = input("Points: ")
try:
    points = int(points)
except ValueError:
    exit_program()
if points < 0 or points > 100:
    exit_program()
if points <= 59:
    grade = "F"
elif points <= 69:
    grade = "D"
elif points <= 79:
    grade = "C"
elif points <= 89:
    grade = "B"
else:
    grade = "A"
if not grade == "F":
    if points % 10 >= 8:
        grade += "+"
    elif points % 10 <= 1:
        grade += "-"
else:
    if points >= 58:
        grade += "+"
    elif points <= 1:
        grade += "-"
print("Note: {:s}".format(grade))
