N = int(input())
lun = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ruiseki = 0
oldlevel = 9
nowlevel = 0
while len(lun) < N:
    for _ in range(oldlevel):
        if lun[ruiseki][-1] != "0":
            lun.append(lun[ruiseki] + str(int(lun[ruiseki][-1]) - 1))
            nowlevel += 1
        lun.append(lun[ruiseki] + lun[ruiseki][-1])
        nowlevel += 1
        if lun[ruiseki][-1] != "9":
            lun.append(lun[ruiseki] + str(int(lun[ruiseki][-1]) + 1))
            nowlevel += 1
        ruiseki += 1
    oldlevel = nowlevel
    nowlevl = 0
print(lun[N - 1])
