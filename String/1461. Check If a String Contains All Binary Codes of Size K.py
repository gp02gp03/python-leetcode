'''
Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "00110", k = 2
Output: true
Example 3:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.

'''


def hasAllCodes(self, s: str, k: int) -> bool:
    res = []
    for i in range(len(s) - k + 1):
        res.append(s[i:i + k])
    #print(res)
    return len(res) == 2**k
