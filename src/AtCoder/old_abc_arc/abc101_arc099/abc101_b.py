N = input()
SN = 0
for i in N:
    SN += int(i)
print('Yes' if int(N) % SN == 0 else 'No')
