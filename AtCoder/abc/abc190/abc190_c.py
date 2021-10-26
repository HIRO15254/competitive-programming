N, M = map(int, input().split(" "))
jyo = []
for i in range(M):
    a, b = map(int, input().split(" "))
    jyo.append([a, b])
K = int(input())
cd = []
for i in range(K):
    c, d = map(int, input().split(" "))
    cd.append([c, d])

ans = 0
for i in range(2**K):
    era = set()
    kans = 0
    for j in range(K):
        if 2**j & i:
            era.add(cd[j][0])
        else:
            era.add(cd[j][1])
    for j in range(M):
        if jyo[j][0] in era and jyo[j][1] in era:
            kans += 1
    ans = max(ans, kans)
print(ans)
