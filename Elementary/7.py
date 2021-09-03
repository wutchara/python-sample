def checkNotPrime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    return flag

n = input("Number: ")
number = int(n)

# lists = []
for i in range(2, number + 1):
    if not checkNotPrime(i):
        print(i, end =" ")
        # lists.append(i)

# print(", ".join(map(str, lists)))
