N = int(input())
S = []
ans = []
for i in range(5):
    S.append(input())
for i in range(N):
    if S[0][i * 4 + 1:i * 4 + 4] == "###":
        if S[1][i * 4 + 1:i * 4 + 4] == "#.#":
            if S[2][i * 4 + 1:i * 4 + 4] == "#.#":
                ans.append('0')
            else:
                if S[3][i * 4 + 1:i * 4 + 4] == "#.#":
                    ans.append('8')
                else:
                    ans.append('9')
        elif S[1][i * 4 + 1:i * 4 + 4] == "..#":
            if S[2][i * 4 + 1:i * 4 + 4] == "..#":
                ans.append('7')
            else:
                if S[3][i * 4 + 1:i * 4 + 4] == "#..":
                    ans.append('2')
                else:
                    ans.append('3')
        else:
            if S[3][i * 4 + 1:i * 4 + 4] == "#.#":
                ans.append('6')
            else:
                ans.append('5')
    elif S[0][i * 4 + 1:i * 4 + 4] == ".#.":
        ans.append('1')
    else:
        ans.append('4')
print("".join(ans))
