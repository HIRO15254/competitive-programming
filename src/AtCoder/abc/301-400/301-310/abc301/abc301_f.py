S = list(input())
Cap_used = []
DD_shape = False
# 0~26: 大文字被りなし, 27: DDxx型 28:DDox型
DP = [0] * 28
DP[0] = 1
for i in range(len(S)):
    if S[i] != "?":
        if S[i].isupper():
            if S[i] in Cap_used:
                DD_shape = True
                DP[27] = sum(DP[0:27])
            else:
                Cap_used.append(S[i])
                DP[1] = 