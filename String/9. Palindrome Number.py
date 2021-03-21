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


def isPalindrome(x):
    x_len = len(str(x))
    x = list(str(x))
    for i in range(x_len):
        #print(x[i],x[-i-1])
        if x[i] != x[-i - 1]:
            return False
    return True


print(isPalindrome(-101))
