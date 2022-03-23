X, Y = map(int, input().split(" "))
ans = 0
now = X
while now <= Y:
    now *= 2
    ans += 1
print(ans)
