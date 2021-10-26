N = int(input())
A = list(map(int, input().split(" ")))
c = [0] * 200
ans = 0

for i in A:
    c[i % 200] += 1
for i in c:
    ans += (i * (i - 1)) // 2
print(ans)
