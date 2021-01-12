'''

Given two binary strings a and b, return their sum as a binary string.
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 




class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, c = [], '0'
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or c == '1':
            ai = a[i] if i >= 0 else '0'
            bj = b[j] if j >= 0 else '0'
            if ai == bj:
                res.append(c)
                c = ai
            else:
                res.append('0' if c == '1' else '1')
            i, j = i - 1, j - 1
        return ''.join(res[::-1])


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]; 



'''