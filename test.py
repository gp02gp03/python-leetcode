def solution(A):
    a = (sorted(A))
    m = max(a)
    res = 0
    if m > 0:
        for i in range(1, m):
            if i not in a:
                res = i
            else:
                res = m + 1
        return res
    else:

        return 1


print(solution([1, 3, 6, 4, 1, 2]))
