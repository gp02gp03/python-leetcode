def generate(umRows):
    res,tmp = [],[1]
    if umRows == 0:
        return []
    else:
        for i in range(umRows):
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
                #print res
                #print tmp
    return res
                    
print(generate(5))
                    
            

'''
1 => [1]
2 => [[1],[1,1]]
3 => [[1],[1,1],[1,2,1]]
4 => [[1],[1,1],[1,2,1],[1,3,3,1]]
5 => [[[1],[1,1],[1,2,1],[1,3,3,1]],[1,4,6,4,1]]
'''