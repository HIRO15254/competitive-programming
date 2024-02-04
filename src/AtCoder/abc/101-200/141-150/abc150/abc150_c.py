def kaijyo(num):
    ans = 1
    for i in range(num):
        ans = ans * (i + 1)
    return ans


N = int(input())
P = list(map(int, input().rstrip().split(" ")))
Q = list(map(int, input().rstrip().split(" ")))
ap = [(i + 1) for i in range(N)]
aq = [(i + 1) for i in range(N)]
Pa = 0
Qa = 0
for i in range(N):
    Pa += ap.index(P[i]) * kaijyo(N - i - 1)
    ap.pop(ap.index(P[i]))
for i in range(N):
    Qa += aq.index(Q[i]) * kaijyo(N - i - 1)
    aq.pop(aq.index(Q[i]))
print(abs(Pa - Qa))
