import sys

sys.setrecursionlimit(2000)
N = int(input())
graph = [[] for _ in range(N)]
d = list(map(int, input().split()))
for i in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append([v - 1, w])
    graph[v - 1].append([u - 1, w])


def solve(now, p):
    p_cost = -1
    ans = []
    for i in graph[now]:
        if i[0] != p:
            ans.append(solve(i[0], now))
        else:
            p_cost = i[1]
        ans.sort(reverse=True)
    # print(now, p, ans, p_cost)
    if d[now] == 0:
        ret = 0
        for i in ans:
            ret += i[2]
        return [0, ret, ret]
    else:
        ans_a = 0
        ans_b = 0
        for i in range(len(ans)):
            if i <= d[now] - 1:
                ans_a += ans[i][1]
                ans_b += ans[i][1]
            elif i == d[now]:
                ans_a += ans[i][2]
                ans_b += ans[i][1]
            else:
                ans_a += ans[i][2]
                ans_b += ans[i][2]
        ans_a += p_cost
        return [max(ans_a - ans_b, 0), max(ans_a, ans_b), ans_b]


print(solve(0, -1)[2])
