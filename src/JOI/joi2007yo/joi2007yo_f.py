a, b = map(int, input().rstrip().split(" "))
n = int(input())

way = [[0 for _ in range(b)]for _ in range(a)]
way[0][0] = 1

koji = []

for i in range(n):
    x, y = list(map(int, input().rstrip().split(" ")))
    koji.append([x - 1, y - 1])

for i in range(a + b):
    for j in range(i + 1):
        if j < a and i - j < b:
            if [j + 1, i - j] not in koji and j + 1 < a:
                way[j + 1][i - j] += way[j][i - j]
            if [j, i - j + 1] not in koji and i - j + 1 < b:
                way[j][i - j + 1] += way[j][i - j]
print(way[a - 1][b - 1])
