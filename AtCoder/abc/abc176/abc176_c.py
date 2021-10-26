N = int(input())
A = list(map(int, input().rstrip().split(" ")))
ans = 0
minnow = A[0]
for i in range(1, N):
    if(minnow > A[i]):
        ans += minnow - A[i]
    else:
        minnow = A[i]
print(ans)
