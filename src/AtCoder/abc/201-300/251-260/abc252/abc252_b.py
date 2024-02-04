N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = max(A)
ret = False
for i in range(N):
    if A[i] == m and (i + 1) in B:
        ret = True
if ret:
    print("Yes")
else:
    print("No")
