N, M = map(int, input().split(" "))
k = 0
p = []
for i in range(M):
    A, B = map(int, input().split(" "))
    if A >= B:
        k += 1
    else:
        p.append((B - A) // 2)
p.sort()
if k >= M - 1:
    print(0)
else:
    print(sum(p[0:M - 1 - k]))
