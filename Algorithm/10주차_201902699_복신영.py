def do(item, value, weight, limit):
    n = len(item)
    opt = [[0 for _ in range(limit + 1)] for _ in range(n + 1)]
    for i in range(n+1):
        for w in range(limit + 1):
            if i == 0 or w == 0:
                opt[i][w] = 0
            elif weight[i-1] > w:
                opt[i][w] = opt[i-1][w]
            else:
                opt[i][w] = max(value[i-1] + opt[i-1][w-weight[i-1]], opt[i-1][w])
    return opt[len(opt)-1][len(opt[0])-1]


def main():
    item = []
    value = []
    weight = []
    n, k = map(int, input().split())
    for i in range(n):
        arr = list(map(int, input().split()))
        item.append(i)
        weight.append(arr[0])
        value.append(arr[1])
    print(do(item, value, weight, k))


if __name__ == '__main__':
    main()
