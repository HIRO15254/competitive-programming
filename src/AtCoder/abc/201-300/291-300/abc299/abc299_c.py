N = int(input())
S = input()
S2 = S.split("-")
S3 = []
if S.count("-") == 0 or S.count("o") == 0:
    print(-1)
    exit()
for i in S2:
    S3.append(len(i))
else:
    print(max(S3))
