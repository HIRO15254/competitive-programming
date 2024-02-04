from collections import deque
Q = int(input())
cache = [1]
for i in range(6 * 10 ** 5):
    cache.append(cache[-1] * 10 % 998244353)
now_ans = 1
now_queue = deque([1])

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        now_ans = (now_ans * 10 + query[1]) % 998244353
        now_queue.append(query[1])
    if query[0] == 2:
        last = now_queue.popleft()
        now_ans = (now_ans + 998244353 * 10 - cache[len(now_queue)] * last) % 998244353
    if query[0] == 3:
        print(now_ans)
