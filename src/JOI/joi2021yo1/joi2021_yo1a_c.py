N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
A.sort()
B.sort()
ans = set()
for i in A:
    if i in B:
        ans.add(i)
ans2 = list(ans)
ans2.sort()
for i in ans2:
    print(i)
