#Write a function to find the longest common prefix string amongst an array of strings.
def longestCommonPrefix(strs):
    strs_len = len(strs)
    if strs_len == 0:
        return ""
    elif strs_len == 1:
        return strs[0]
    else:
        if len(strs[0]) == 0 or len(strs[1]) == 0:
            return ""
    tmp, res, count, same, tmp_sec = str(strs[0]), [], 0, 0, str(strs[1])
    if tmp[0] != tmp_sec[0]:
        return ""
    for i in range(1, strs_len):
        if len(tmp) > len(strs[i]):
            count = len(strs[i])
        else:
            count = len(tmp)
            same = 0
            for j in range(count):
                if tmp[j] == strs[i][j]:
                    same += 1
                else:
                    break
    tmp = strs[i][:same]
    return ''.join(tmp[:same])


print(longestCommonPrefix(['abcd', 'abccc', 'abdec']))
