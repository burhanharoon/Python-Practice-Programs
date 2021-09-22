"""
Title: Program to convert temperatures to and from celsius, fahrenheit
Description: Input the complete string i.e. 32c and it will automatically convert this to Fahrenheit and vice versa
Expected Input: 37c , 37C , 100f , 100F , <number><symbol:C:F>
Expected Output: 100.0 Farenheit in Celcius is: 34.0
"""

again = True


def tryAgain():
    tryAgain = input('Try Again (Y/N): ')
    tryAgain = tryAgain.lower()
    if 'y' in tryAgain:
        again = True
    else:
        again = False


while again:
    temp = input(
        '\nPlease enter the temperature in Celcius or Fahrenheit and plese add c or f along with it: ')

    temp = temp.lower()  # Incase the user has used Uppercase C or F

    if 'c' in temp:
        index = temp.index('c')
        # Fetching the number part of the input string
        inCelcius = float(temp[0:index])
        inFahrenheit = inCelcius*1.8+32
        print('{} Celcius in Farenheit is: {}\n'.format(inCelcius, inFahrenheit))
        tryAgain()

    elif 'f' in temp:
        index = temp.index('f')
        inFahrenheit = float(temp[0:index])
        inCelcius = (inFahrenheit-32)/2
        print('{} Farenheit in Celcius is: {}\n'.format(inFahrenheit, inCelcius))
        tryAgain()

    else:
        print("Please enter the correct value")
        tryAgain()
