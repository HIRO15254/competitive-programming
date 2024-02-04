import math


N, A, B = map(int, input().split())
ans = int(N * (N + 1) // 2)
A_count = N // A
A_sum = int(A * A_count * (A_count + 1) // 2)
B_count = N // B
B_sum = int(B * B_count * (B_count + 1) // 2)
C = int(A * B / math.gcd(A, B))
C_count = N // C
C_sum = int(C * C_count * (C_count + 1) // 2)
print(ans - A_sum - B_sum + C_sum)
