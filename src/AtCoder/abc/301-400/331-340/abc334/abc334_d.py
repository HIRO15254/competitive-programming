N, Q = map(int, input().split())
R = list(map(int, input().split())) + [10 ** 18 + 1]
R.sort()
R_s = [0] * (N + 2)
for i in range(N + 1):
    R_s[i + 1] = R_s[i] + R[i]


def BinarySearch(X, ng=N+1, ok=0):
    while (abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        if R_s[mid] <= X:
            ok = mid
        else:
            ng = mid
    return ok


for i in range(Q):
    X = int(input())
    print(BinarySearch(X))
