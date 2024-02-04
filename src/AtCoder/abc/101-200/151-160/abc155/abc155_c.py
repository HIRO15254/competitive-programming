input_num = int(input())
dic = {}
strlist = []
strlist2 = []
maxi = 1
for i in range(input_num):
    strlist.append(input())
for i in range(input_num):
    if dic.setdefault(strlist[i], 0) != 0:
        dic[strlist[i]] += 1
        if dic[strlist[i]] > maxi:
            maxi = dic[strlist[i]]
    else:
        dic[strlist[i]] = 1
        strlist2.append(strlist[i])
strlist2.sort()
for i in range(len(strlist2)):
    if dic[strlist2[i]] == maxi:
        print(strlist2[i])
