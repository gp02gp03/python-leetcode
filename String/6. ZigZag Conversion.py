def convert(s,numRows):
    s_len = len(s)
    if s_len == 0:
        return ""
    if numRows == 1:
        return s
    n = numRows * 2 - 2
    tmp = []
    for i in range(numRows):
        tmp.append("")
    for i in range(s_len):
        lineNumber = (i % n)
        if lineNumber < numRows:
            tmp[lineNumber] += s[i]
        else:
            tmp[2*numRows - lineNumber - 2] += s[i]
    return ''.join(tmp)

print(convert("PAYPALISHIRING",3))

