def isPalindrome(num):
    reversed_num=0
    original=num
    while num!=0:
        digit=num%10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if original==reversed_num:
        return True
    else:
        return False
print(isPalindrome(11))
print(isPalindrome(10))
print(isPalindrome(101))