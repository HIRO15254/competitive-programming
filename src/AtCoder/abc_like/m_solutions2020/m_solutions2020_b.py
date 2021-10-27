A, B, C = map(int, input().rstrip().split(" "))
K = int(input())
ans = False
for i in range(K):
    if A >= B:
        B *= 2
    elif B >= C:
        C *= 2
    else:
        ans = True
        break
if A < B < C:
    ans = True
if ans:
    print("Yes")
else:
    print("No")
