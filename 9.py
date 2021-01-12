def isPalindrome(x):
    res = 0
    a = x / 10 
    b = x % 10
    print(a)
    print(b)
    while a > 0:
        a = a / 10
        c = a
print(isPalindrome(121))


'''
Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false

'''