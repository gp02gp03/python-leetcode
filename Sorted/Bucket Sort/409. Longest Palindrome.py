'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


Example 2:

Input: s = "a"
Output: 1


Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''


def longestPalindrome(s):
    from collections import Counter
    counter = Counter(s)
    res = 0
    f = 0
    for v in counter.values():
        if v % 2 == 0:
            res += v
        else:
            res += v - 1
            f = 1
    return res + f


print(longestPalindrome("abccccdd"))