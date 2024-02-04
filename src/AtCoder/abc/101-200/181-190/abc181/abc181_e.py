N, M = map(int, input().split(" "))
H = list(map(int, input().split(" ")))
W = list(map(int, input().split(" ")))
H.sort()
W.sort()
h_c = 0
add = []
add_sum = [0]
add_rev = [0]
even = []
even_sum = [0]
even_rev = [0]

for i in range(N - 1):
    if i % 2 == 0:
        add.append(H[i + 1] - H[i])
    else:
        even.append(H[i + 1] - H[i])

for i in range(int((N - 1) / 2)):
    even_sum.append(even_sum[-1] + even[i])
    add_sum.append(add_sum[-1] + add[i])
    even_rev.append(even_rev[-1] + even[len(even) - 1 - i])
    add_rev.append(add_rev[-1] + add[len(add) - 1 - i])

ans = 10 ** 18
for w in W:
    while h_c != N and w > H[h_c]:
        h_c += 1
    ans2 = 0
    if h_c % 2 == 0:
        ans2 += H[h_c] - w
        p = int(h_c / 2)
        q = int((N - 1 - h_c) / 2)
    else:
        ans2 += w - H[h_c - 1]
        p = int((h_c - 1) / 2)
        q = int((N - h_c) / 2)
    ans2 += add_sum[p] + even_rev[q]

    ans = min(ans, ans2)
print(ans)
