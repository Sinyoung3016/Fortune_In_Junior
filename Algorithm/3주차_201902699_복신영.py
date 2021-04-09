from itertools import *


def prime(k):
    if k < 2: return False
    for i in range(2, k):
        if k % i == 0: return False
    return True


inputStr = list(input())

pList = [(permutations(inputStr, i)) for i in range(1, len(inputStr) + 1)]
valuesInOneSet = set(i for j in pList for i in j)
set2Str = ["".join(i) for i in valuesInOneSet]

answer = 0
for n in set2Str:
    n = int(n)
    if prime(n): answer += 1

print(answer)



