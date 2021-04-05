'''
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
'''

def longestValidParentheses(s):
    res = 0
    stack = [-1]
    for i,j in enumerate(s):
        if j == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res,i - stack[-1])
    return res

print(longestValidParentheses(")()())"))
