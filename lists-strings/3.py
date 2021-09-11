def isContains(lists, item):
    return item in lists

array = [1, 2, 3, 4, 5, 6]
element = 4
print("Lists: ", array)
print("Find '{}'({}) in Lists: '{}' => {}".format(element, type(element), array, isContains(array, element)))
print('--------------------------------')

element = '4'
print("Lists: ", array)
print("Find '{}'({}) in Lists: '{}' => {}".format(element, type(element), array, isContains(array, element)))
print('--------------------------------')


element = 'GG'
print("Lists: ", array)
print("Find '{}'({}) in Lists: '{}' => {}".format(element, type(element), array, isContains(array, element)))