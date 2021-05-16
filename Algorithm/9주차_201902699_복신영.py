def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    limit = k * arr[0]
    arr = [i for i in arr if i < limit+1]
    count = list()

    for i in arr:
        c = 0
        for j in arr:
            c += i // j
        count.append(c)

    index = 0
    for i in range(len(count)):
        if k < count[i]:
            index = i
            break
    index -= 1
    answer = arr[index]
    need = k - count[index]

    for i in range(index-1, -1, -1):
        answer += (need//count[i]) * arr[i]
        need -= (need // count[i]) * count[i]

    if answer%arr[0] != 0:
        answer -= (answer%arr[0])

    print(answer)


if __name__ == '__main__':
    main()
