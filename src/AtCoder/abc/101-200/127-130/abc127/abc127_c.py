N, M = map(int, input().rstrip().split(" "))
ans_min = 0
ans_max = N
for i in range(M):
    L, R = map(int, input().rstrip().split(" "))
    ans_min = max(L, ans_min)
    ans_max = min(R, ans_max)
print(max(0, ans_max - ans_min + 1))
