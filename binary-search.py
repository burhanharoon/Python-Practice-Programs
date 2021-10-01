import math


def binarySearch(array, low, high, key):
    if low > high:
        return -1
    else:
        mid = int(low+high/2)
        math.floor(mid)
        print("Low {} High {} mid {}".format(low, high, mid))
        if key == array[mid]:
            return True
        elif key > array[mid]:
            return binarySearch(array, mid+1, high, key)
        elif key < array[mid]:
            return binarySearch(array, low, mid-1, key)


array = [1, 2, 3, 4]
x = int(3)
print(binarySearch(array, 0, len(array)-1, x))
