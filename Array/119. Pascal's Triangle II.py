def getRow(rowIndex):
    res,tmp = [],[1]
    for i in range(rowIndex+1):
        if i==0:
            res.append([1])
        elif i==1:
            res.append([1,1])
        else:
            cur = res[-1]
            cur_Len = len(cur)
            tmp = [1]
            for j in range(cur_Len):
                if j+1 < cur_Len:
                    tmp.append(cur[j] + cur[j+1])
            tmp.append(1)  
            res.append(tmp)
    print res
    return res[rowIndex]
                    
print(getRow(5))



'''
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

'''
                    