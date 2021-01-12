def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    res = dic[s[0]]
    for i in range(1,len(s)):
        if dic[s[i-1]]>=dic[s[i]]:
            res = res + dic[s[i]]
        else:
            res = res + dic[s[i]] - 2*dic[s[i-1]]
    return res



print(romanToInt("IV"))

print(romanToInt("III"))
