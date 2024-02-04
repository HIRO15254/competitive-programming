def dfs(v):
    s = set()
    emp_c = 0
    ans = False
    cant_win = False
    for i in C[v]:
        ret = dfs(i)
        ans = ans or ret[0]
        emp_c += ret[1]
        s |= ret[2]
        cant_win = cant_win or ret[3]
    if A[v] == -1:
        emp_c += 1
    elif A[v] < K:
        s.add(A[v])
    if A[v] == K:
        cant_win = True
    if ((K - len(s)) <= 1) and (emp_c <= 1) and (not cant_win) and (emp_c >= (K - len(s))):
        ans = True
    # print(v, ans, emp_c, K - len(s))
    return (ans, emp_c, s, cant_win)


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    C = [[] for _ in range(N)]
    P = [0] + list(map(int, input().split()))
    A = list(map(int, input().split()))
    for i in range(1, N):
        C[P[i] - 1].append(i)
    if dfs(0)[0]:
        print("Alice")
    else:
        print("Bob")
