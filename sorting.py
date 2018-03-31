# Jerome C. Reyes BSCpE

print('Sorting')


def Selection_Sort(xList):
    for i in range(len(xList)):
        least = i
        for k in range(i + 1, len(xList)):
            if xList[k] < xList[least]:
                least = k

        swap(xList, least, i)


def swap(B, o, y):
    temp = B[o]
    B[o] = B[y]
    B[y] = temp


my_list = [55.32, 13.12, 1.84, 35.64, 5.66, 88, 101.1, 8.97, 4.12, 36.28, 43.5]
Selection_Sort(my_list)
print(my_list)


print('Searching')

def binary_search(value, target):
    low = 0
    mid = len(value) / 2
    upper = len(value)

    if len(value) == 1:
        if value[0] == target:
            print(target)
            return value[0]
        else:
            return False
    if target == value[mid]:
        print(value[mid])
        return mid
    else:
        if mid > low:
            value_l = value[0:mid]
            binary_search(value_l, target)

        if upper > mid:
            value_2 = value[mid:len(value)]
            binary_search(value_2, target)


    if __name__ == "__main__":
        a = [4, 5, 7, 8, 9, 4, 3, 2, 5, 6, 1]
        binary_search(a, 9)