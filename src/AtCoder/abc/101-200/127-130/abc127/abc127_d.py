N, M = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
A.sort(reverse=True)
Q = []
for i in range(M):
    B, C = map(int, input().rstrip().split(" "))
    Q.append([C, B])
Q.sort(reverse=True)

p = 0
j = 0
while p < N and j < M:
    for i in range(Q[j][1]):
        if i + p > N:
            break
        A.append(Q[j][0])
    p += Q[j][1]
    j += 1
ans = 0
A.sort(reverse=True)

for i in range(N):
    ans += A[i]

print(ans)
