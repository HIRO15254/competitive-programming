N = int(input())
A = list(map(int, input().split(" ")))
A.sort()
ans = 0
rui_wa = [0]
for i in range(N):
    rui_wa.append(rui_wa[-1] + A[i])
for i in range(N):
    ans += (A[i] * i) - rui_wa[i]
    ans += (rui_wa[-1] - rui_wa[i + 1]) - (A[i] * (N - 1 - i))
print(ans // 2)
