N = int(input())
S = list(input())
J = []
O = []
I = []
for i in S:
    if i == "J":
        J.append("J")
    elif i == "O":
        O.append("O")
    else:
        I.append("I")
print("".join(J) + "".join(O) + "".join(I))
