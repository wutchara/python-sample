def getTwenty(num):
    list = []
    for i in range(num, (num + 20) + 1):
        list.append(i*i)
    return list

array = [1, 2, 3, 4, 5, 6, 7]
print("Lists:", array)
for num in array:
    print("Perfect array of {} is {}".format(num, getTwenty(num)))