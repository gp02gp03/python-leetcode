'''
Input: s = "anagram", t = "nagaram"
Output: true
'''
def isAnagram(s, t):
    def count(x):
        m = {}
        for c in x:
            if c in m:
                m[c] = m[c] + 1
            else:
                m[c] = 1
        return m
    return count(s) == count(t)

print(isAnagram("anagram","nagaram"))
        