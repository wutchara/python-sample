def isPalindrome(str):
    return str == str[::-1]


strList = ['noon', 'stats', '123456', '12321', '111']
for testStr in strList:
    print("Check String: ", testStr)
    print("This strring is Palindrome: ", isPalindrome(testStr))
    print("-----------------------")