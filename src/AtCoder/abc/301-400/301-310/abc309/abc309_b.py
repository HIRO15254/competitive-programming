N = int(input())
S = []
for i in range(N):
    S.append(list(input()))

S_next = ""
S_next_old = ""


def repl(x, y, val):
    ret = S[x][y]
    S[x][y] = val
    return ret


S_next = S[0][0]
for i in range(N - 1):
    S_next = repl(0, i + 1, S_next)
for i in range(N - 1):
    S_next = repl(i + 1, N - 1, S_next)
for i in range(N - 1):
    S_next = repl(N - 1, N - 2 - i, S_next)
for i in range(N - 1):
    S_next = repl(N - 2 - i, 0, S_next)

for i in range(N):
    print("".join(S[i]))
