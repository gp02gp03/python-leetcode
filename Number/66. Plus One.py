def plusOne(digits):
    plus = 1
    for i in range(len(digits)-1, -1, -1):
        if digits[i] + plus > 9:
            digits[i] = 0
            plus = 1
        else:
            digits[i] = digits[i] + plus
            plus = 0
    if plus == 1:
        digits.insert(0, 1)
    return digits

print(plusOne([1,2,3]))

'''
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]

'''
    