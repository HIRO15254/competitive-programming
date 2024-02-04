K = [0 for _ in range(10 ** 5 + 10)]
N = int(input())
A = list(map(int, input().rstrip().split(" ")))
ans = 0
for i in A:
    K[i] += 1
    ans += i
Q = int(input())
for i in range(Q):
    B, C = map(int, input().rstrip().split(" "))
    q = K[B]
    K[B] = 0
    K[C] += q
    ans += (C - B) * q
    print(ans)
