'''
Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.

'''


def minRemoveToMakeValid(s):
    res = []
    count = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
            res.append(s[i])
        elif s[i] == ")":
            if count > 0:
                count -= 1
                res.append(s[i])
        else:
            res.append(s[i])
    for i in range(len(res) - 1, -1, -1):
        if count == 0:
            break
        if res[i] == "(":
            count -= 1
            res[i] = ""
    return ''.join(res)


print(minRemoveToMakeValid("(a(b(c)d)"))
print(minRemoveToMakeValid("lee(t(c)o)de)"))
