import sys

t = int(input())
for _ in range(t):
    input = list(sys.stdin.readline().rstrip().split('B'))
    answer = 0
    for i in input:
        l = len(i)
        for j in range(l):
            answer += (j+1)
    print(answer)
