from collections import deque


def R(x, y):
    return x + 1, y


def L(x, y):
    return x - 1, y


def U(x, y):
    return x, y - 1


def D(x, y):
    return x, y + 1


def move(c, x, y):
    if c == 'R':
        return R(x, y)
    elif c == 'L':
        return L(x, y)
    elif c == 'U':
        return U(x, y)
    elif c == 'D':
        return D(x, y)
    else:
        return x, y


def BFS(graph, fro, to):
    visited = [-1 for _ in range(len(graph))]
    queue = deque([fro])
    visited[fro] = 0

    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == -1:
                visited[i] = visited[n] + 1
                if i == to:
                    return visited[i]
                queue.append(i)
    return 0


def main():
    answer = 0
    n, m = map(int, input().split())
    arr = [list(input().split()) for _ in range(n)]
    listofmat = list()

    fill = 1
    find = False
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):  # Y
        for j in range(m):  # X
            target = matrix[i][j]
            if target == 0 and find == False:
                x = i
                y = j
                matrix[x][y] = fill
                l = [(x, y)]
                while True:
                    y, x = move(arr[x][y], y, x)
                    if 0 <= y < n and 0 <= x < m:
                        matrix[x][y] = fill
                        l.append((x, y))
                    else:
                        listofmat.append(l)
                        break
                    if y == n - 1 and x == m - 1:
                        matrix[x][y] = fill
                        find = True
                        break
                fill += 1

    outer_l = list(list() for _ in range(fill))
    for j in listofmat:
        for i in j:
            target = matrix[i[0]][i[1]]
            if 0 <= i[1] < m and 0 < i[0] < n + 1:
                if matrix[i[0] - 1][i[1]] not in outer_l[target]:
                    outer_l[target].append(matrix[i[0] - 1][i[1]])
            if 0 < i[1] < m + 1 and 0 <= i[0] < n:
                if matrix[i[0]][i[1] - 1] not in outer_l[target]:
                    outer_l[target].append(matrix[i[0]][i[1] - 1])
            if 0 <= i[1] < m and -1 <= i[0] < n - 1:
                if matrix[i[0] + 1][i[1]] not in outer_l[target]:
                    outer_l[target].append(matrix[i[0] + 1][i[1]])
            if -1 <= i[1] < m - 1 and 0 <= i[0] < n:
                if matrix[i[0]][i[1] + 1] not in outer_l[target]:
                    outer_l[target].append(matrix[i[0]][i[1] + 1])

    answer = BFS(outer_l, 1, fill-1)
    print(answer)


if __name__ == '__main__':
    main()
