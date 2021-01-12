def isValid(s):
    stack = []
    dic = {"(": ")", "[": "]", "{": "}"}
    for c in s:
        if stack and dic.get(stack[-1], '') == c:
            stack.pop()
        else:
            stack.append(c)
    return not stack


print(isValid("()[]{}"))