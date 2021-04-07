'''
Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true

'''

from collections import Counter
def halvesAreAlike(s):
    l = len(s) // 2
    CountLeftS = Counter(s[:l].lower())
    CountRightS = Counter(s[l:].lower())
    cnt1 = 0
    cnt2 = 0
    for i in ('a','e','i','o','u'):
        cnt1 += CountLeftS[i]
        cnt2 += CountRightS[i]
    return cnt1 == cnt2

print(halvesAreAlike("book"))
