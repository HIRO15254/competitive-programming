K = int(input())
M, N = map(int, input().rstrip().split(" "))
ans = False
for i in range(M, N + 1):
    if i % K == 0:
        ans = True
if(ans):
    print("OK")
else:
    print("NG")
