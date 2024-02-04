N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def solve(a):
    left = []
    for i in range(N):
        if Q[i] - A[i] * a >= 0:
            left.append(Q[i] - A[i] * a)
        else:
            return -1
    b_min = 10 ** 18
    for i in range(N):
        if B[i] != 0:
            b_min = min(b_min, left[i] // B[i])
    return b_min + a


a = 0
ans = 0
while solve(a) != -1:
    ans = max(ans, solve(a))
    a += 1

print(ans)
