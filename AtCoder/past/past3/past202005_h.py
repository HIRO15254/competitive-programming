N, L = map(int, input().rstrip().split(" "))
x = set(map(int, input().rstrip().split(" ")))
T1, T2, T5 = map(int, input().rstrip().split(" "))

kodo = [[0], [2, 3], [2, 1, 1, 3]]
T4 = (T1 + T2) // 2
T3 = (T1 + T2) // 2
times = [T1, T2, T3, T4, T5]
DP = [10 ** 9 for i in range(L * 2 + 5)]
DP[0] = 0
ans = 10 ** 9
for i in range(L):
    for i2 in range(3):
        time = 0
        for i3 in range(len(kodo[i2])):
            time += times[kodo[i2][i3]]
            if (kodo[i2][i3] == 0 or kodo[i2][i3] == 3) and i + i3 + 1 in x:
                time += times[4]
            if i + i3 + 1 == L:
                if ans > DP[i] + time:
                    ans = DP[i] + time
        if DP[i + len(kodo[i2])] > DP[i] + time:
            DP[i + len(kodo[i2])] = DP[i] + time
print(ans)
