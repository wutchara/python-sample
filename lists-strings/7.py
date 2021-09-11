def sumFor(lists):
    total = 0
    for num in lists:
        total = total + num
    return total

def sumWhile(lists):
    total = 0
    i = 0
    listCount = len(lists)
    while i < listCount:
        total += lists[i]
        i += 1
    return total

def sumRecursion(lists, index = 0):
    if (index >= len(lists)):
        return 0

    return lists[index] + sumRecursion(lists, index + 1)


array = [1, 2, 3, 4, 5, 6, 7]
print("For loop:", sumFor(array))
print("While loop:", sumWhile(array))
print("Recursion:", sumRecursion(array))