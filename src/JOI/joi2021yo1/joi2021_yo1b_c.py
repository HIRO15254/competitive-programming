N = int(input())
A = list(map(int, input().split(" ")))
ma = max(A)
ans1 = 0
for i in A:
    if i == ma:
        print(ans1)
        print(sum(A) - ma - ans1)
        break
    else:
        ans1 += i
