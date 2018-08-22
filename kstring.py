def isPalindrome(str):
    len = len(str) - 1
    for i in range(0, len + 1):
        if str[i] != str[len - 1]:
            return False
    return True
