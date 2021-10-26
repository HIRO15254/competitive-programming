N = int(input())
Q = int(input())
row = [i for i in range(N)]
line = [i for i in range(N)]
rev = False
ans = 0
for i in range(Q):
    s = list(map(int, input().rstrip().split(" ")))
    if s[0] == 1:
        if rev:
            rev_a = line[s[1] - 1]
            rev_b = line[s[2] - 1]
            line[s[1] - 1] = rev_b
            line[s[2] - 1] = rev_a
        else:
            rev_a = row[s[1] - 1]
            rev_b = row[s[2] - 1]
            row[s[1] - 1] = rev_b
            row[s[2] - 1] = rev_a
    elif s[0] == 2:
        if rev is False:
            rev_a = line[s[1] - 1]
            rev_b = line[s[2] - 1]
            line[s[1] - 1] = rev_b
            line[s[2] - 1] = rev_a
        else:
            rev_a = row[s[1] - 1]
            rev_b = row[s[2] - 1]
            row[s[1] - 1] = rev_b
            row[s[2] - 1] = rev_a
    elif s[0] == 3:
        if rev:
            rev = False
        else:
            rev = True
    else:
        if rev is False:
            print(row[s[1] - 1] * N + line[s[2] - 1])
        else:
            print(line[s[1] - 1] + row[s[2] - 1] * N)
