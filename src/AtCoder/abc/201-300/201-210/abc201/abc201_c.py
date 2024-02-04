S = input()
d = [0] * 4
ans = 0
for i in range(10000):
    for j in range(4):
        d[j] = (i // (10 ** j)) % 10
    for j in range(10):
        if S[j] == "o":
            if j not in d:
                break
        elif S[j] == "x":
            if j in d:
                break
    else:
        ans += 1
print(ans)
