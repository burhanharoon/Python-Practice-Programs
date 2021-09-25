lines = []
while True:
    l = input()
    if l:
        lines.append(l.lower())
    else:
        break

for x in lines:
    print(x)