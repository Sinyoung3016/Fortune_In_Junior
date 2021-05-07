from functools import cmp_to_key


def fun(x, y):
    x_l = len(x)
    y_l = len(y)
    if x_l == 1 or y_l == 1:
        if x[0] > y[0]:
            return 1
        elif x[0] < y[0]:
            return -1
        else:
            return 0
    elif x_l != 1 and y_l != 1:
        return fun(x[1:], y[1:])


def main():
    n = int(input())
    inp = input().split()
    arr = [list('') for _ in range(10)]

    for i in inp:
        arr[int(i[0])].append(i)
    for i in range(10):
        arr[i].sort(key=cmp_to_key(fun))

    answerList = []
    for i in arr:
        for j in i:
            answerList.append(j)

    answer = ""
    for i in range(len(answerList)-1, -1, -1):
        answer += answerList[i]

    print(answer)


if __name__ == '__main__':
    main()
