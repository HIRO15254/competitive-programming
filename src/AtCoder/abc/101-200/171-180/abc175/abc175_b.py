N = int(input())
L = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            if (max(L[i], L[j], L[k]) * 2 < L[i] + L[j] + L[k]) and (L[i] != L[j]) and (L[j] != L[k]) and (L[k] != L[i]):
                ans += 1
print(ans)
