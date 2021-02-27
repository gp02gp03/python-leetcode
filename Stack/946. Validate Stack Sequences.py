'''
Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Constraints:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
'''


def validateStackSequences(pushed, popped):
    stack = []
    index = 0
    for i in range(len(pushed)):
        stack.append(pushed[i])
        while stack and stack[-1] == popped[index]:
            stack.pop()
            index += 1
    return len(popped) == index


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(validateStackSequences(pushed, popped))
