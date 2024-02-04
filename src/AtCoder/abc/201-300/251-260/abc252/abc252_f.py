import heapq

N, L = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
if sum(A) != L:
    A.append(L - sum(A))
    N += 1
heapq.heapify(A)
for i in range(N - 1):
    a = heapq.heappop(A)
    b = heapq.heappop(A)
    ans += a + b
    heapq.heappush(A, a + b)
print(ans)
