N = int(input())
A = list(map(int, input().rstrip().split(" ")))
ans = 0
counter = 1
for i in range(N - 1):
    if A[i] <= A[i + 1]:
        counter += 1
    else:
        if counter > ans:
            ans = counter
        counter = 1
if counter > ans:
    ans = counter
print(ans)
