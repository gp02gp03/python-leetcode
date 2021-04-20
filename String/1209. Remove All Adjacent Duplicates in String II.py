'''
Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"

Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

'''



def removeDuplicates(s, k):
    stack = [['#',0]]
    res = ""
    for c in s:
        if c == stack[-1][0]:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c,1])
    for c in stack[1:]:
        res = res + str(c[0]*c[1])
    return res

print(removeDuplicates("deeedbbcccbdaa",3))