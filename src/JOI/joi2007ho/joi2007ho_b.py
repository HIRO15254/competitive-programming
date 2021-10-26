n, k = map(int, input().split(" "))
A = []
for i in range(k):
    A.append(int(input()))
A.sort()
A.append(100001)

counter = 0
a = 0
b = 0
Q = []
if A[0] == 0:
    counter += 1
for i in range(1, n + 1):
    if A[counter] == i:
        if b != 0:
            Q.append([a, b])
            a = 0
            b = 0
        a += 1
        counter += 1
    else:
        b += 1
Q.append([a, b])
Q.append([0, 0])
ans = 0

if A[0] != 0:
    for i in range(len(Q)):
        ans = max(ans, Q[i][0])
else:
    for i in range(len(Q)):
        if Q[i][1] == 1:
            ans = max(Q[i][0] + Q[i + 1][0] + 1, ans)
        else:
            ans = max(Q[i][0] + 1, ans)

print(ans)
