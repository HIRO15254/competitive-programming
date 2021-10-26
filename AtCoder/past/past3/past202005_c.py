A, R, N = map(int, input().rstrip().split(" "))
ans = A
flag = False
for i in range(N - 1):
    ans = ans * R
    if ans > 10 ** 9:
        flag = True
        break
if flag:
    print("large")
else:
    print(ans)
