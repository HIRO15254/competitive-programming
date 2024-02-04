N, K = map(int, input().split())
A = list(map(int, input().split()))

f_count = 0
b_count = N * (N + 1) // 2 + 1
tmp = sorted(A)

for i in range(N):
    tmp.remove(A[i])
    k = 0
    while (k <= N - i - 2) and (tmp[k] < A[i]):
        f_count += 1
        if (f_count == K):
            j = A.index(tmp[k])
            print(" ".join(map(str, A[:i] + A[i:j + 1][::-1] + A[j + 1:])))
            exit()
        k += 1
    k = N - i - 2
    while (k >= 0) and (tmp[k] > A[i]):
        b_count -= 1
        if (b_count == K):
            j = A.index(tmp[k])
            print(" ".join(map(str, A[:i] + A[i:j + 1][::-1] + A[j + 1:])))
            exit()
        k -= 1
print(" ".join(map(str, A)))
