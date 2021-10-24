N, T = map(int, input().rstrip().split(" "))
A = list(map(int, input().rstrip().split(" ")))
max_ra = [0 for i in range(len(A) + 1)]
ans = 0
k = 0
for i in range(len(A) - 1, -1, -1):
    if max_ra[i + 1] < A[i]:
        max_ra[i] = A[i]
    else:
        max_ra[i] = max_ra[i + 1]
for i in range(len(A)):
    if max_ra[i] - A[i] > k:
        ans = 1
        k = max_ra[i] - A[i]
    elif max_ra[i] - A[i] == k:
        ans += 1
print(ans)
