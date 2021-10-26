H = int(input())
ans = 0
counter = 0
while H > 0:
    H = int(H / 2)
    ans += 2 ** counter
    counter += 1
print(ans)
