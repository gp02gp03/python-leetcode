'''
Example 1:

Input: s = "ababa"
Output: 1
Explanation: String is already palindrome
Example 2:

Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "". 
Remove palindromic subsequence "a" then "bb".
Example 3:

Input: s = "baabb"
Output: 2
Explanation: "baabb" -> "b" -> "". 
Remove palindromic subsequence "baab" then "b".
'''


def removePalindromeSub(s):
    if not s:
        return 0
    l = len(s)
    for i in range(l):
        if s[i] != s[-i - 1]:
            return 2
    return 1


print(removePalindromeSub("baabb"))