import itertools

S1 = list(input())
S2 = list(input())
S3 = list(input())
d = set()
for i in S1:
    d.add(i)
for i in S2:
    d.add(i)
for i in S3:
    d.add(i)
if len(d) > 10:
    print("UNSOLVABLE")
else:
    ld = list(d)
    L1 = []
    L2 = []
    L3 = []
    for i in S1:
        L1.append(ld.index(i))
    L1.reverse()
    for i in S2:
        L2.append(ld.index(i))
    L2.reverse()
    for i in S3:
        L3.append(ld.index(i))
    L3.reverse()
    for i in itertools.permutations(range(10)):
        if(i[L1[-1]] == 0 or i[L2[-1]] == 0 or i[L3[-1]] == 0):
            continue
        I1 = 0
        for j in range(len(L1)):
            I1 += i[L1[j]] * (10 ** j)
        I2 = 0
        for j in range(len(L2)):
            I2 += i[L2[j]] * (10 ** j)
        I3 = 0
        for j in range(len(L3)):
            I3 += i[L3[j]] * (10 ** j)
        if I1 + I2 == I3:
            print(I1)
            print(I2)
            print(I3)
            break
    else:
        print("UNSOLVABLE")
