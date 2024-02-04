N = int(input())
c = list(input())
r = 0
w = 0
ans = 0
for i in c:
    if i == "R":
        r += 1
    else:
        w += 1
for i in range(r):
    if c[i] != "R":
        ans += 1
print(ans)
