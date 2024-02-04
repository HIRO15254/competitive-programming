X, K, D = map(int, input().split())
ans = 0
if abs(X) > K * D:
    ans = abs(abs(X) - K * D)
else:
    if (K - (abs(X) // D)) % 2 == 0:
        ans = abs(abs(X) - (abs(X) // D) * D)
    else:
        ans = abs(abs(X) - (abs(X) // D + 1) * D)
print(ans)
