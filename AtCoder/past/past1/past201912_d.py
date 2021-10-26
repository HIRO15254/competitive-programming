n = int(input())
s = [0 for _ in range(n)]
ansa = 0
ansb = 0
for i in range(n):
    s[int(input()) - 1] += 1
for i in range(n):
    if s[i] == 2:
        ansa = i + 1
    elif s[i] == 0:
        ansb = i + 1
if ansa + ansb == 0:
    print("Correct")
else:
    print(str(ansa) + " " + str(ansb))
