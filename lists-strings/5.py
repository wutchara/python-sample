def total(lists):
    total = 0
    for i in range(0, len(lists)):    
        total = total + lists[i]
    return total

array = [1, 2, 3, 4, 5, 6, 7]
print("Lists: ", array)
print("Total array: ", total(array))