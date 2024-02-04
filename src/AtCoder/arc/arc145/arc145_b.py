def solve(N, A, B):
    if A <= B:
        return max(N - A + 1, 0)
    else:
        p = max(N - A + 1, 0) // A
        q = max(N - A + 1, 0) % A
        return p * B + min(q, B)


N, A, B = map(int, input().split())
print(solve(N, A, B))
