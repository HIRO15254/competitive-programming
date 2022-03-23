from collections import deque

N = int(input())
A = list(map(int, input().split()))

q = deque()
ans = 0
for i in A:
    if not q:
        q.append([i, 1])
    else:
        t = q.pop()
        if t[0] != i:
            q.append(t)
            q.append([i, 1])
        else:
            t[1] += 1
            if t[0] == t[1]:
                ans -= t[1]
            else:
                q.append(t)
    ans += 1
    print(ans)