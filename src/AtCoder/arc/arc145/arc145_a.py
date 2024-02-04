def solve(S):
    if len(S) == 2:
        if S[0] == S[1]:
            return True
    else:
        if S[0] == "B" or S[-1] == "A" and len(S) > 2:
            return True
    return False

N = int(input())
S = list(input())
if solve(S):
    print("Yes")
else:
    print("No")
