S = int(input())

q = set()

ans = S
for i in range(2, 10**5):
    if i in q:
        continue
    k = i * i
    while k <= S:
        if k <= 10 ** 5:
            q.add(k)
        ans -= 1
        k *= i
print(ans)
