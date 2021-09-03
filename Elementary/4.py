n = input("Maximum number(n): ")
print("You input: " + n)

# convert string to int
number = int(n)

list = []

# (1, number]
for i in range(1, number + 1):
    if (i % 3 == 0 or i % 5 ==0):
        list.append(i)

# print list
print(*list, sep = ", ") 
