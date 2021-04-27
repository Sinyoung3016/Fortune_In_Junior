n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_count = n
for i in range(n):
    count_start = False
    count = 0
    for j in range(n):
        if arr[i][j] == 1 and count_start:
            if count == 0:
                continue
            if min_count > count:
                min_count = count
            count_start = False
            count = 0
        if arr[i][j] == 1 and not count_start:
            count_start = True
        if arr[i][j] == 0 and count_start:
            count += 1

for j in range(n):
    count_start = False
    count = 0
    for i in range(n):
        if arr[i][j] == 1 and count_start:
            if count == 0:
                continue
            if min_count > count:
                min_count = count
            count_start = False
            count = 0
        if arr[i][j] == 1 and not count_start:
            count_start = True
        if arr[i][j] == 0 and count_start:
            count += 1

print(min_count)
