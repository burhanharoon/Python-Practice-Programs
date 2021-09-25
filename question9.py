fibonacci = [0, 1]
for x in range(48):
    newFiboNum = fibonacci[x] + fibonacci[x+1]
    fibonacci.append(newFiboNum)
print(fibonacci)
