N = int(input())
A = list(map(int, input().split()))

ans_min = 0
ans_now = 0

for i in range(N):
    ans_now += A[i]
    ans_min = min(ans_min, ans_now)

print(-ans_min + ans_now)
