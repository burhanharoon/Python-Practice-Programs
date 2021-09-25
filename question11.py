rows = int(input('No of rows: '))
columns = int(input('No of Columns: '))
twoDimenArray = [[0 for x in range(columns)] for y in range(rows)]

for row in range(rows):
    for column in range(columns):
        twoDimenArray[row][column] = row*column

print(twoDimenArray)
