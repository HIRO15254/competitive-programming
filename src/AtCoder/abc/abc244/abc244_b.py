S = [[1, 0], [0, -1], [-1, 0], [0, 1]]
N = int(input())
T = input()
ans = [0, 0]
now = 0
for A in T:
    if A == "S":
        ans[0] += S[now % 4][0]
        ans[1] += S[now % 4][1]
    else:
        now += 1
print(ans[0], ans[1])