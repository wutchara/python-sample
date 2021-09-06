if 1 > 2:
    print("Five is greater than two!")
else:
    print("---------")
    if 5 > 2:
        print("Five is greater than two!xxx")
        if 9 > 2:
            print("Five is greater than two!yyyyyy")
print(".............................................")

x = 5
y = 'Hello, World!'
y2 = y + ": {}"
z = "y: {}, x: {}".format(y, x)

print("X, Y: ", x, y)
print("y: {}, x: {}".format(y, x))
print("z: ", z)
print(y2.format(x))

print(type(y))
print(type(y2))

# x, y, z = "Orange", 5, "Cherry"
if 5 > 2:
    zz = x
    zz += 5
    print("--", zz)
# print(y)
# print(z)

print("****", zz)
print("****", x)
