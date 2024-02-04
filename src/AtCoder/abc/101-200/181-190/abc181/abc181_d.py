S = list(input())
c = [S.count(str(i)) for i in range(10)]
ans = False
for j in range(0, 1000, 8):
    q = [str(j).count(str(i)) for i in range(10)]
    q[0] += max(min(3, sum(c)) - sum(q), 0)
    for i in range(10):
        if c[i] < q[i]:
            break
    else:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
