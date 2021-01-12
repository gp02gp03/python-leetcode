def compareVersion(version1, version2):
    v1_list, v2_list = version1.split("."), version2.split(".")
    v1_len, v2_len = len(v1_list), len(v2_list)
    tmp, diff = 0, 0
    count = 0
    if v1_len > v2_len:
        tmp = v1_len
        diff = v1_len - v2_len
    elif v1_len < v2_len:
        tmp = v2_len
        diff = v2_len - v1_len
    else:
        tmp = v1_len
    if diff > 0:
        while diff > 0:
            v2_list.append(0)
            diff -= 1
    else:
        while diff < 0:
            v1_list.append(0)
            diff += 1
    for i in range(tmp):
        v1 = int(v1_list[i])
        v2 = int(v2_list[i])
    if v1 < v2:
        return -1
    elif v1 > v2:
        return 1
    return 0


print(compareVersion("0.1", "1.1"))
print(compareVersion("1.0.1", "1"))
