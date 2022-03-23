S = input() + "T"
X, Y = map(int, input().split(" "))


def dp(start, lis, target):
    ans = set()
    ans2 = set()
    ans.add(start)
    for i in lis:
        for j in ans:
            ans2.add(j + i)
            ans2.add(j - i)
        ans = ans2
        ans2 = set()
    return target in ans


x = []
y = []
now = "x"
count = 0
for i in S:
    if i == "F":
        count += 1
    elif i == "T":
        if now == "x":
            x.append(count)
            now = "y"
        else:
            y.append(count)
            now = "x"
        count = 0
start = 0
if S[0] != "T":
    start = x[0]
    x = x[1:]
if dp(start, x, X) and dp(0, y, Y):
    print("Yes")
else:
    print("No")
