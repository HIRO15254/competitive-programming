def kaisen(s):
    ret = []
    if len(s) % 2 == 1:
        s = s * 2
    for i in range(len(s) // 2):
        if s[i * 2] == s[i * 2 + 1]:
            ret.append(s[i * 2])
        elif (s[i * 2] == "R" and s[i * 2 + 1] == "S") or (s[i * 2] == "P" and s[i * 2 + 1] == "R") or (s[i * 2] == "S" and s[i * 2 + 1] == "P"):
            ret.append(s[i * 2])
        else:
            ret.append(s[i * 2 + 1])
    return ret


n, k = map(int, input().split(" "))
s = list(input())
for i in range(k):
    s2 = kaisen(s)
    s = s2
print(s[0])
