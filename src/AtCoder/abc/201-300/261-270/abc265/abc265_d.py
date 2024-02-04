import itertools

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
A2 = [0] + list(itertools.accumulate(A))
A2_set = set(A2)
for i in range(N):
    if A2[i] + P in A2_set and A2[i] + P + Q in A2_set and A2[i] + P + Q + R in A2_set:
        print("Yes")
        break
else:
    print("No")
