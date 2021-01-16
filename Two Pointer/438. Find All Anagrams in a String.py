'''
Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''


def findAnagrams(s, p):
    def transfer(c):
        return ord(c) - 97

    res = []
    counterS = [0] * 26
    counterP = [0] * 26
    l = len(p) - 1
    for c in p:
        counterP[transfer(c)] += 1

    # 先取兩個
    for c in s[:l]:
        counterS[transfer(c)] += 1

    #print(counterP)
    #print(counterS)

    #取s剩下的,往後加一個 & 往前減一個後再重新計算
    for i, c in enumerate(s[l:]):
        counterS[transfer(c)] += 1
        #print(counterS)
        if counterS == counterP:
            res.append(i)
        counterS[transfer(s[i])] -= 1
    return res


print(findAnagrams("cbaebabacd", "abc"))