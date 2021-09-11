def getOddPosition(lists):
    oddArray = []
    for i in range(1, len(lists), 2):    
        oddArray.append(lists[i])
    return oddArray

array = [1, 2, 3, 4, 5, 6, 7]
print("Lists: ", array)
print("Odd position array: ", getOddPosition(array))