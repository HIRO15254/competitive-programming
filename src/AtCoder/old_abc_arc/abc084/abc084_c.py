N = int(input())
STATIONS = []
for i in range(N - 1):
    C, S, F = map(int, input().split(" "))
    STATIONS.append([C, S, F])
ans = [0] * N
for i in range(N - 1):
    for j in range(i + 1):
        C, S, F = STATIONS[i]
        ans[j] = max(S, (max(ans[j] - S - 1, -1) // F + 1) * F + S) + C
for i in range(N):
    print(ans[i])
