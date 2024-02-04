N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Query = []
Q_Schedule = [[] for _ in range(N + 1)]
ans = [-1] * Q
now = [0] * (N + 1)
for i in range(Q):
    L, R, X = map(int, input().split())
    Q_Schedule[L - 1].append(i)
    Q_Schedule[R].append(i)
    Query.append(X)


def Q_update(n):
    for i in Q_Schedule[n]:
        if ans[i] == -1:
            ans[i] = now[Query[i]]
        else:
            ans[i] = now[Query[i]] - ans[i]


Q_update(0)
for i in range(N):
    now[A[i]] += 1
    Q_update(i + 1)
for i in range(Q):
    print(ans[i])
