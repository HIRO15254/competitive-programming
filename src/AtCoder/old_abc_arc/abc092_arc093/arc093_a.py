N = int(input())
A = list(map(int, input().split()))
A = [0] + A + [0]
sa = []
sa_2 = []

for i in range(N + 1):
    sa.append(abs(A[i] - A[i + 1]))
ans = sum(sa)
for i in range(N):
    sa_2.append(abs(A[i] - A[i + 2]))
for i in range(N):
    print(ans - sa[i] - sa[i + 1] + sa_2[i])