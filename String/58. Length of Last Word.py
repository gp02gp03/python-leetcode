def lengthOfLastWord(s):
    if len(str(s)) == 0:
        return 0 
    slist = list(s.split(' '))
    for i in range(len(slist)):
        res = len(slist.pop())
        if res > 0:
            return res
    return 0


print(lengthOfLastWord("Hello world"))
