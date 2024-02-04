def kaibun(s):
    ans = True
    for i in range(int(len(s) / 2)):
        if s[i] != s[-1 * i - 1]:
            ans = False
            break
    return(ans)


inp = input()
N = len(inp)
a = int((N - 1) / 2)
b = int((N + 3) / 2 - 1)
inp_a = inp[:a]
inp_b = inp[b:]
if kaibun(inp) and kaibun(inp_a) and kaibun(inp_b):
    print("Yes")
else:
    print("No")
