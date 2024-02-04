N, K = map(int, input().split())
med = []
now = 0
for i in range(N):
    a, b = map(int, input().split())
    med.append((a, -b))
    now += b
med.sort()
if now <= K:
    print(1)
    exit()
for i in range(N):
    now += med[i][1]
    if now <= K:
        print(med[i][0] + 1)
        exit()
