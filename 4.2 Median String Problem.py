import itertools
import math

def difference(pat1, pat2):
    if(pat1 == pat2):
       return 0
    tmp = 0
    i = 0
    for j in pat1:
        if j != pat2[i]:
            tmp+=1
        i+=1
    return tmp

def eachPattern(k):
    patterns = []
    each = itertools.product('ATGC', repeat=k)
    for i in each:
        tmp = ''.join(i)
        patterns.append(tmp)
    return patterns

def d(DNA, pattern, k):
    res = 0
    hd = []
    for st in DNA:
        for i in range(len(st) - k + 1):
            hd.append(difference(pattern, st[i:i+k]))
        res += min(hd)
        hd = []
    return res

def MedianString(DNA, k):
    diff = math.inf
    patterns = eachPattern(k)
    for pattern in patterns:
        if diff >= d(DNA, pattern, k):
            diff = d(DNA, pattern, k)
            res = pattern
    return res


k = int(input())
DNA = []
for i in range(10):
    DNA.append(input())


print(MedianString(DNA, k))