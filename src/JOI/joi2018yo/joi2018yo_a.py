N, A, B, C, D = map(int, input().split(" "))
q = []
q.append((N - 1) // A * B + B)
q.append((N - 1) // C * D + D)

print(min(q))
