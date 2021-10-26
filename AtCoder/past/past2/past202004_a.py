N, M = input().split(" ")
if N[0] == "B":
    Ni = int(N[1]) * -1
else:
    Ni = int(N[0]) - 1

if M[0] == "B":
    Mi = int(M[1]) * -1
else:
    Mi = int(M[0]) - 1

print(abs(Ni - Mi))
