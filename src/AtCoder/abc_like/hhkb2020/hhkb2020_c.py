N = int(input())
p = list(map(int, input().split(" ")))
A = [-1 for _ in range(2 * 10 ** 5 + 1)]
for i in range(N):
    if A[p[i]] == -1:
        A[p[i]] = i
now = 0
for i in range(N):
    while A[now] != -1 and A[now] <= i:
        now += 1
    print(now)
