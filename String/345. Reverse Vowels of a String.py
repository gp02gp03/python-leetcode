def reverseVowels(s: str) -> str:
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    sList = list(s)
    temp = []
    for i in range(len(s)):
        if s[i] in vowel:
            temp.append(s[i])   
    temp.reverse()
    print(temp)
    j=0     
    for i in range(len(sList)):
        if sList[i] in vowel:
            sList[i]= temp[j]
            j= j+1
    return ''.join(sList)

print(reverseVowels("hello"))
print(reverseVowels("aA"))