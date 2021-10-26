N = int(input())
q = int(input())
c = 1
r = []
ans = 10 ** 10
for i in range(N - 1):
    p = int(input())
    if p == q:
        c += 1
    else:
        r.append([q, c])
        c = 1
        q = p
r.append([q, c])
for i in range(len(r)):
    if r[i][1] == 1:
        j = 1
        k_ans = N
        while i - j >= 0 and i + j < len(r) and r[i - j][0] == r[i + j][0] and (r[i - j][1] + r[i + j][1] >= 4 or (r[i - j][1] + r[i + j][1] >= 3 and j == 1)):
            k_ans -= r[i - j][1] + r[i + j][1]
            if j == 1:
                k_ans -= r[i][1]
            j += 1
        if k_ans < ans:
            ans = k_ans
        j = 1
        k_ans = N
        if i >= 1 and r[i - 1][1] == 3 and r[i - 1][0] != r[i + 1][0]:
            while i - 1 - j >= 0 and i + j < len(r) and r[i - 1 - j][0] == r[i + j][0] and (r[i - 1 - j][1] + r[i + j][1] >= 4 or (r[i - 1 - j][1] + r[i + j][1] >= 3 and j == 1)):
                k_ans -= r[i - 1 - j][1] + r[i + j][1]
                if j == 1:
                    k_ans -= r[i][1] + r[i - 1][1]
                j += 1
        if k_ans < ans:
            ans = k_ans
        j = 1
        k_ans = N
        if i < len(r) - 1 and r[i + 1][1] == 3 and r[i - 1][0] != r[i + 1][0]:
            while i - j >= 0 and i + 1 + j < len(r) and r[i - j][0] == r[i + 1 + j][0] and (r[i - j][1] + r[i + 1 + j][1] >= 4 or (r[i - j][1] + r[i + 1 + j][1] >= 3 and j == 1)):
                k_ans -= r[i - j][1] + r[i + 1 + j][1]
                if j == 1:
                    k_ans -= r[i][1] + r[i + 1][1]
                j += 1
        if k_ans < ans:
            ans = k_ans
print(ans)
