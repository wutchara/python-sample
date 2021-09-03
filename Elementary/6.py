print("--------------------")
print("Multiplication table")
print("--------------------")

# [2, 12]
for m in range(2, 13):
    print("-------------------- {} --------------------".format(m))
    for n in range(1, 13):
        print("{} x {}\t= {}".format(m, n, m*n))
