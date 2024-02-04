A, B, K = map(int, input().split())
ans = 0
now = A
while now < B:
    ans += 1
    now *= K
print(ans)
