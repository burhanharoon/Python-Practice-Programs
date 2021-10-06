import math


def binarySearch(array, low, high, key):
    int(low)
    int(high)
    if low > high:
        return -1
    else:
        mid = int(math.floor(low+high/2))
        print('low {} high {} mid {}'.format(low, high, mid))
        if key == array[mid]:
            return True
        elif key > array[mid]:
            return binarySearch(array, mid, high, key)
        elif key < array[mid]:
            return binarySearch(array, low, mid, key)


array = [1, 2, 3, 4]
x = int(0)
print(binarySearch(array, 0, len(array)-1, x))
