
n = int(input())
first = [0 for _ in range(n+1)]
second = [0 for _ in range(n+1)]
first[0] = second[0] = n+1

for _ in range(n):
    a, b = map(int, input().split(' '))
    first[a] = b
    second[b] = a

answerSet = set()
for i in range(1, n):
    if first[i] < first[i - 1]:
        answerSet.add((i, first[i]))
    else:
        break

for i in range(1, n):
    if second[i] < second[i-1]:
        answerSet.add((second[i], i))
    else:
        break

answer = len(answerSet)
print(answer)
