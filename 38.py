def Solution(n):
    if n <= 1:
        return 1
    else:
        count = 1
        result = '1'
        for i in range(2, n + 1):
            if len(result) <= 1:
                result = str(count) + result
            else:
                #print(result)
                for i in range(len(result)):
                    if i < len(result) - 1:
                        if result[i] == result[i + 1]:
                            count += 1
                            result = str(count) + result[i]
                        else:
                            result = str(count) + result
                    else:
                        if result[i] == result[i - 1]:
                            count += 1
                        else:
                            result = str(count) + result

    ##return result


print(Solution(4))