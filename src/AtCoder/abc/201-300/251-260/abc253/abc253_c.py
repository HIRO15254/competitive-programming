import heapq
a = []
Q = int(input())
ma = 0
dic = dict()
for _ in range(Q):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        heapq.heappush(a, inp[1])
    elif inp[0] == 2:
        if inp[1] in dic:
            if dic[inp[1]] > inp[2]:
                dic[inp[1]] -= inp[2]
            else:
                dic[inp[1]] = 0
                heapq.heappop(a)