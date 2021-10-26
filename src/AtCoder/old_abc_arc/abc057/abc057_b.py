N, M = map(int, input().rstrip().split(" "))
stu = [[] for _ in range(N)]
che = [[] for _ in range(M)]
for i in range(N):
    stu[i] = list(map(int, input().rstrip().split(" ")))
for i in range(M):
    che[i] = list(map(int, input().rstrip().split(" ")))
for i in range(N):
    ansnum = 0
    ansdis = 10 ** 9
    for i2 in range(M):
        if abs(che[i2][0] - stu[i][0]) + abs(che[i2][1] - stu[i][1]) < ansdis:
            ansnum = i2 + 1
            ansdis = abs(che[i2][0] - stu[i][0]) + abs(che[i2][1] - stu[i][1])
    print(ansnum)
