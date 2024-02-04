N, K = map(int, input().split())
A = list(map(int, input().split()))
if min(A[:K]) >= max(A[K:]):
    print(-1)
else:
    s = [[A[K - 1], 1]]
    t = [[0, 0], [A[K], 0]]
    for i in range(K - 2, -1, -1):
        if A[i] < s[-1][0]:
            s.append([A[i], K - i])
    for i in range(K + 1, N):
        if A[i] > t[-1][0]:
            t.append([A[i], i - K])
    t.append([10 ** 9 + 1, 10 ** 9 + 1])
    ans = 10 ** 9
    for i in s:
        ng = 0
        ok = len(t) - 1
        while(abs(ng - ok) > 1):
            mid = (ok + ng) // 2
            if i[0] < t[mid][0]:
                ok = mid
            else:
                ng = mid
        ans = min(ans, i[1] + t[ok][1])
    print(ans)
