'''
Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]

'''


def wordSubsets(A, B):
    from collections import Counter
    from collections import defaultdict
    target = defaultdict(int)
    for word in B:
        for k,v in Counter(word).items():
            target[k] = max(target[k],v)
            #print(target[k])
    res = []
    for word in A:
        ct = Counter(word)
        for k,v in target.items():
            if k not in ct or v > ct[k]:
                break
        else:
            res.append(word)
    return res


print(
    wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"],
                ["e", "oo"]))
