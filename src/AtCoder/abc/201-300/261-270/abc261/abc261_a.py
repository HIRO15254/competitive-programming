L1, R1, L2, R2 = map(int, input().split())
ans = [0] * 100
for i in range(L1, R1):
    ans[i] += 1
for i in range(L2, R2):
    ans[i] += 1
print(ans.count(2))
