S = list(input())
T = list(input())
S_count = []
T_count = []

alp = "abcdefghijklmnopqrstuvwxyz"
for s in alp:
    S_count.append(S.count(s))
    T_count.append(T.count(s))
S_left = S.count("@")
T_left = T.count("@")

for i in range(26):
    if (S_count[i] != T_count[i]):
        if not (alp[i] in "atcoder"):
            print("No")
            exit()
        else:
            if (S_count[i] > T_count[i]):
                T_left -= S_count[i] - T_count[i]
            else:
                S_left -= T_count[i] - S_count[i]
            if (S_left < 0 or T_left < 0):
                print("No")
                exit()
print("Yes")
