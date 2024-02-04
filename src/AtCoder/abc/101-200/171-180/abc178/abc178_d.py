S = int(input())
p = [0 for _ in range(max(4, S + 1))]
p[3] = 1
for i in range(4, S + 1):
    p[i] += 1
    for j in range(1, i - 2):
        p[i] += p[j]
        p[i] %= 10 ** 9 + 7
print(p[S])
