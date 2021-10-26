N = int(input())
q = 1000 - N
ans = 0
for i in range(3):
    k = (q // (10 ** i)) % 10
    if k >= 5:
        ans += k - 4
    else:
        ans += k
print(ans)
