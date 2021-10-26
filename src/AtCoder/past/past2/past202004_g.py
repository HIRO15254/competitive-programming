Q = int(input())
s = []
now = [0, 0]
alp = "abcdefghijklmnopqrstuvwxyz"

for i in range(Q):
    inp = input().split(" ")
    if inp[0] == "1":
        s.append([int(inp[2]), alp.find(inp[1])])
    if inp[0] == "2":
        count = [0] * 26
        left = int(inp[1])
        while now[0] != len(s) and left != 0:
            if s[now[0]][0] - now[1] < left:
                left -= s[now[0]][0] - now[1]
                count[s[now[0]][1]] += s[now[0]][0] - now[1]
                now = [now[0] + 1, 0]
            else:
                count[s[now[0]][1]] += left
                now = [now[0], now[1] + left]
                left = 0
        ans = 0
        for j in range(26):
            ans += count[j] ** 2
        print(ans)
