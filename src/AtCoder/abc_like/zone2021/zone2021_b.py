N, D, H = map(int, input().split(" "))
ans = 0
for i in range(N):
    d, h = map(int, input().split(" "))
    ans = max(ans, (H - (H - h) * (D / (D - d))))
print(ans)
