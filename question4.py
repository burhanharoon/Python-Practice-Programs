y = 1
z = 2

for line in range(9):
    a = y
    if a > 5:
        a -= z
        z += 2
    for x in range(a):
        print("*", end="")
    print("\n")
    y += 1
