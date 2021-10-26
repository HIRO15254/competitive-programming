S = input()
JOI = 0
IOI = 0
for i in range(len(S) - 2):
    if S[i:i + 3] == "JOI":
        JOI += 1
    elif S[i:i + 3] == "IOI":
        IOI += 1

print(JOI)
print(IOI)
