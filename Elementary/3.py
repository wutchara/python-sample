name = input("Enter your name: ")
whiteLists = ['alice', 'bob']

if name.lower() in whiteLists:
    print("Welcome '{}'".format(name))
else:
    print("............")