'''
Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1

'''


def firstBadVersion(n):
    low = 1
    high = n

    def isBadVersion(n):
        return True

    while low <= high:
        mid = (low + high) // 2
        if isBadVersion(mid):
            if mid == 1 or not isBadVersion(mid - 1):
                return mid
            high = mid - 1
        else:
            low = mid + 1
    return None
