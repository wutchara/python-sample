list1 = ["a", "b", "c"]
list2 = [1, 2, 3, 4, 5]


def isExists(list, index):
    try:
        list[index]
        return True
    except IndexError:
        return False


def combineArr(arr1, arr2):
    first = arr1.copy()
    second = arr2.copy()
    result = []

    for index, item in enumerate(first):
        result.append(item)

        if isExists(second, index):
            result.append(second[index])

    print("xxx", [0, 1, 2, 3][2:])

    # If 'second' still contains items
    for item in second[len(first):]:
        result.append(item)

    return result


print(list1, " , ", list2, " => ", combineArr(list1, list2))
