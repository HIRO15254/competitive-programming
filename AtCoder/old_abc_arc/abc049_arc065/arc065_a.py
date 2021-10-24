moji = 0
S = input()
Slen = len(S)
check = ["dreamer", "eraser", "dream", "erase"]
flag = True
while flag:
    flag = False
    for i in range(4):
        if len(S) - moji >= len(check[i]) and S[Slen - moji - len(check[i]):Slen - moji] == check[i]:
            moji += len(check[i])
            flag = True
            break
if moji == len(S):
    print("YES")
else:
    print("NO")
