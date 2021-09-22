temp = input(
    'Please enter the temperature in Celcius or Farenheit and remember to add C or F along with it: ')
if 'C' or 'c' in temp:
    if 'c' in temp:
        
    tempValue = float(temp[0:index])
    x = tempValue*1.8+32
    print(x)

# 33c
# 33C
