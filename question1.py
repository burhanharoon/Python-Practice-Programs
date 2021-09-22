number = 1500
while number <= 2700:
    if (number % 7 == 0) and (number % 5 == 0):
        print(number)
        number += 1
    else:
        number += 1
