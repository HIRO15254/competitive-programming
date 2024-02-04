N = int(input())
cop = dict()
abr = dict()
inp = []
for _ in range(N):
    m = int(input())
    inp.append([])
    for _ in range(m):
        p, e = map(int, input().split())
        if p not in cop:
            cop[p] = e
            abr[p] = True
        else:
            if cop[p] == e:
                abr[p] = False
            elif cop[p] < e:
                cop[p] = e
                abr[p] = True
        inp[-1].append([p, e])
se = set()
for i in inp:
    po = []
    for j in i:
        if cop[j[0]] == j[1] and abr[j[0]]:
            po.append(j[0])
    se.add(tuple(po))
print(len(se))
