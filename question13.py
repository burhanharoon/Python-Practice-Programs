binary = [int(x) for x in input("Enter the list items seperated by a space: ").split(',')]
decimal = [int(str(x), 2) for x in binary]

for index, value in enumerate(decimal):
    if value % 5 == 0:
        print(binary[index])
