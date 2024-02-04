N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)
ans = 0
for i in range((N - 1) // D + 1):
    # print(F[i*D:i*D+D])
    ans += min(sum(F[i * D:i * D + D]), P)
print(ans)
