S = input()
T = input()
for i in range(len(S), -1, -1):
    if i + len(T) <= len(S):
        for j in range(len(T)):
            if S[i + j] != T[j] and S[i + j] != "?":
                break
        else:
            S = S.replace("?", "a")
            print(S[:i] + T + S[i + len(T):])
            break
else:
    print("UNRESTORABLE")
