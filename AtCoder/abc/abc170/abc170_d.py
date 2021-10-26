N = int(input())
ans = 0
A = list(map(int, input().rstrip().split(" ")))
A.sort()
A2 = [True for _ in range(A[-1] + 1)]
for i in range(len(A)):
    k = A[i] * 2
    if A2[A[i]]:
        if i != 0 and A[i - 1] == A[i]:
            A2[A[i]] = False
        while(k < len(A2)):
            A2[k] = False
            k += A[i]
for i in A:
    if A2[i]:
        ans += 1
print(ans)
