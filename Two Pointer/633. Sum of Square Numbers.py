'''
Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true
'''

'''
雙指針法
1. 宣告兩指針 left從0開始 right從根號c開始
2. 判斷a平方加b平方是否大於c 小於c則left加一  否則right減一
3. 等於c則回傳True 都沒找到回傳false
'''


def judgeSquareSum(c):
    left, right = 0, int(c**0.5)
    while left <= right:
        cur = left*left + right * right
        if c > cur:
            left += 1
        elif c < cur:
            right -= 1
        else:
            return True
    return False


print(judgeSquareSum(5))
