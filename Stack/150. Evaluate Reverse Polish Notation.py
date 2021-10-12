'''
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''


def evalRPN(tokens):
    stack = []
    options = ['+', '-', '*', '/']
    for i in tokens:
        if i not in options:
            stack.append(int(i))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if i == '+':
                stack.append(n1+n2)
            elif i == '-':
                stack.append(n1-n2)
            elif i == '*':
                stack.append(n1*n2)
            else:
                tmp = n1//n2
                tmp = tmp + 1 if tmp < 0 and n1 % n2 != 0 else tmp
                stack.append(tmp)
    return stack[0]


print(evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
