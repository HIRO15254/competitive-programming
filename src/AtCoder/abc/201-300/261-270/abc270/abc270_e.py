N, K = map(int, input().split())
K2 = K
A = list(map(int, input().split()))
A2 = [0] + sorted(A)

ans = []
for i in range(N):
    if K2 > (N - i) * (A2[i + 1] - A2[i]):
        K2 -= (N - i) * (A2[i + 1] - A2[i])
    else:
        minus = A2[i] + K2 // (N - i)
        left = K2 % (N - i)
        for i in range(N):
            if A[i] > minus:
                if left > 0:
                    ans.append(A[i] - minus - 1)
                    left -= 1
                else:
                    ans.append(A[i] - minus)
            else:
                ans.append(0)
        print(" ".join(map(str, ans)))
        break
