N = int(input())
A = list(map(int, input().split()))
ans = 0
l = [0] * 401
for i in A:
    l[i + 200] += 1
for i in range(401):
    for j in range(401):
        ans += l[i] * l[j] * (abs(i - j)**2)
print(ans // 2)
