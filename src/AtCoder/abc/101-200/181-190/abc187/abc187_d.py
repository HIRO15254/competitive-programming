N = int(input())
t = 0
s = []
for _ in range(N):
    A, B = map(int, input().split(" "))
    s.append(A * 2 + B)
    t += A
s.sort()
s.reverse()
s2 = 0
ans = 0
while t >= s2:
    s2 += s[ans]
    ans += 1
print(ans)
