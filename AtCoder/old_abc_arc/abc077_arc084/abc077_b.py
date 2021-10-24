N = int(input())
ans = 0
while ans ** 2 <= N:
    ans += 1
print((ans - 1) ** 2)
