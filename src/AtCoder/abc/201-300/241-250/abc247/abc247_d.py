from collections import deque

que = deque()
Q = int(input())
for i in range(Q):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        que.appendleft([inp[1], inp[2]])
    else:
        left = inp[1]
        ans = 0
        while left != 0:
            pop = que.pop()
            if left <= pop[1]:
                que.append([pop[0], pop[1] - left])
                ans += left * pop[0]
                left = 0
            else:
                ans += pop[0] * pop[1]
                left -= pop[1]
        print(ans)
