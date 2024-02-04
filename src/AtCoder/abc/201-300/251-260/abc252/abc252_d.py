import itertools

N = int(input())
A = list(map(int, input().split()))
A.sort()
A.append(-1)
n = []
last_a = A[0]
counter = 1
for i in A[1:]:
    if i != last_a:
        n.append(counter)
        counter = 1
    else:
        counter += 1
    last_a = i
n.sort()
q = dict()
for i in n:
    if i in q:
        q[i] += 1
    else:
        q[i] = 1
ans = 0
print(list(itertools.combinations_with_replacement(q.keys, 3)))
for k in list(itertools.combinations_with_replacement(q.keys, 3)):
    p = k[0] * k[1] * k[2]
    if k[0] == k[1]:
        if k[1] == k[2]:
            if q[k[0]] >= 3:
                ans += p * q[k[0]] * (q[k[0]] - 1) * (q[k[0]] - 2) // 6
        else:
            if q[k[0]] >= 2:
                ans += p * q[k[0]] * (q[k[0]] - 1) * q[k[2]] // 2
    elif k[1] == k[2]:
        if q[k[2]] >= 2:
            ans += p * q[k[0]] * (q[k[2]] - 1) * q[k[2]] // 2
    else:
        ans += p * q[k[0]] * q[k[1]] * q[k[2]]
print(ans)
