n = input("Maximum number(n): ")
print("You input: " + n)

# convert string to int
number = int(n)
sum = 0
product = 1
for i in range(1, number + 1):
    sum += i
    product *= i

print("SUM: {}\nProduct: {}".format(sum, product))
