SA = list(input())
SB = list(input())
SC = list(input())
A = 0
B = 0
C = 0
ans = ""
turn = "a"
while ans == "":
    if turn == "a":
        if A == len(SA):
            ans = "A"
        else:
            turn = SA[A]
        A += 1
    if turn == "b":
        if B == len(SB):
            ans = "B"
        else:
            turn = SB[B]
        B += 1
    if turn == "c":
        if C == len(SC):
            ans = "C"
        else:
            turn = SC[C]
        C += 1
print(ans)
