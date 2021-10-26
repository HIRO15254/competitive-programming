N = int(input())
C = list(map(int, input().split(" ")))
C.sort()
ans = 1
for i in range(len(C)):
    ans *= C[i] - i
    ans %= 10**9 + 7
print(ans)
