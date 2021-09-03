import random

def printSelectedNumber(start, end):
    print("------------------------")
    for i in range(start, end + 1):
        print(i, end=" ")
    print("\n------------------------")

print("Please aenter n and m to use the scope(n, m)")
n = input("n: ")
m = input("m: ")

lower = int(n)
upper = int(m)

if m <= n:
    print("Invalid input (n, m)")
else:
    target = random.randrange(lower, upper, 1)
    # print("target: {}".format(target))

    while True:
        printSelectedNumber(lower, upper)
        userSelected = input("Please select number: ")
        userNumber = int(userSelected)
        if userNumber in range(lower, upper + 1):
            if userNumber > target:
                print("My number is lower than {}. Guess lower ->".format(userNumber))
                upper = userNumber - 1
            elif userNumber < target:
                print("My number is higher than {}. Guess higher <-".format(userNumber))
                lower = userNumber + 1
            else:
                print("Yes! That's my number!!")
                break;