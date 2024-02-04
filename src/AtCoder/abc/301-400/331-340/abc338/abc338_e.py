from collections import deque
N = int(input())

t = [0] * (2 * N)

for i in range(N):
    a, b = map(int, input().split())
    t[a - 1] = i
    t[b - 1] = i

stack = deque()
for i in range(2 * N):
    if stack:
        p = stack.pop()
        if p != t[i]:
            stack.append(p)
            stack.append(t[i])
    else:
        stack.append(t[i])
if stack:
    print('Yes')
else:
    print('No')
